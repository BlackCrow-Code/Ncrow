# ===== Imports =====
import socket                                   # for TCP socket connections (port scanning) and DNS resolution
import argparse                                 # for parsing command-line arguments
from concurrent.futures import ThreadPoolExecutor  # for running the scan function across multiple threads
import os                                       # used for os._exit(0) on force-exit (Ctrl+C)
import logging                                  # for printing formatted [*] info logs
from rich.console import Console                # for colored/styled terminal output
from rich.rule import Rule                      # for printing horizontal separator lines
import pyfiglet                                 # for generating the ASCII art banner ("ncrow")
import json                                     # for writing scan results to a JSON output file
from queue import Queue                         # thread-safe queue to distribute ports among worker threads
from urllib.parse import urlparse               # to extract hostname from a URL target
import requests                                 # for HTTP requests used in server detection (-s option)

# -----> CLI Arguments - Control the tool from terminal
parser = argparse.ArgumentParser(description="Ncrow-PortScanner")
parser.add_argument("-t", "--target", required=True, help="Url or IP_Address")  # target host/URL/IP (required)
parser.add_argument("-p", "--port", nargs=2, type=int, default=[1, 1024], help="Start with port [Space] finish with port")  # port range, default 1-1024
parser.add_argument("-a", "--all", action="store_true", help="Scan all ports")  # flag: scan all 65535 ports instead of the range
parser.add_argument("-T", "--threads", default=50, type=int, help="Number of threads 300 limit")  # number of scanning threads (capped at 300)
parser.add_argument("-s", "--server", action="store_true", help="Server INF")  # flag: try to detect the "Server" HTTP header
parser.add_argument("-oj", "--outputJSON", type=str, help=" save discovered to (JSON) file")  # optional path to save results as JSON
parser.add_argument("-on", "--outputNORMAL", type=str, help="save discovered to (NORMAL) file")  # optional path to save results as plain text
args = parser.parse_args()  # parse the actual arguments passed by the user

# ===== Shared data structures across threads =====
ports = Queue()        # thread-safe queue holding all port numbers to be scanned
json_file = []         # list that collects results (as dicts) to later dump into JSON
normal_file = []       # list that collects results (as strings) to later write into a plain text file

# 65,535 ports
if args.threads > 300:  # enforce a hard cap on thread count to avoid abuse/resource exhaustion
    args.threads = 300

if args.all:  # if the user requested a full scan, override the port range with 1-65535
    start, end = 1, 65536
else:
    start, end = args.port[0], args.port[1] + 1  # otherwise use the user-provided range (end is inclusive, so +1)

# ===== Banner / startup info =====
console = Console()  # rich console object used for styled printing
logging.basicConfig(level=logging.INFO, format="[*]%(message)s")  # configure logging format like "[*] message"
Ncrow = pyfiglet.figlet_format("ncrow", font="slant")  # generate ASCII art text "ncrow" in slant font
console.print(f"[cyan]{Ncrow}[/cyan]")  # print the ASCII banner in cyan
logging.info(f"Target: {args.target}")  # log the scan target
logging.info(f"Port Scan: {'all ports(65,535)' if args.all else args.port}")  # log which ports will be scanned
logging.info(f"Number of Threads: {args.threads if args.threads != 50 else f'default ({args.threads})'}")  # log thread count (note default value)
logging.info(f"Server [INF]: {'True' if args.server else 'False'}")  # log whether server detection is enabled
console.print(Rule())  # print a horizontal separator line

# ===== Resolve target hostname to IP =====
target = urlparse(args.target).hostname or args.target  # extract hostname from URL if given, else use target as-is

try:
    target_ip = socket.gethostbyname(target)  # resolve the hostname/IP to an IPv4 address
except socket.gaierror:
    console.print("[bold red][!]Can't resolve hostname (DNS error)[/bold red]")  # DNS resolution failed
    exit(1)  # stop the program since scanning can't continue without a valid IP

s = requests.Session()  # reusable HTTP session for the optional server-detection request

# -----> Server Detection (Only Once)
result_server = "Server: Not Found"  # default value if server detection is off or fails

if args.server:  # only run this block if the -s/--server flag was passed
    try:
        url = args.target

        
        if not url.startswith(("http://", "https://")):  # ensure the URL has a scheme, default to http
            url = "http://" + url

        response = s.get(url, timeout=3)  # send a quick HTTP GET request to grab response headers
        result_server = response.headers.get("Server", "Server: Not Found")  # extract the "Server" header if present

    except requests.RequestException:
        result_server = "Server: Connection Failed"  # handle any request error (timeout, connection refused, etc.)

# ===== Fill the queue with all ports to scan =====
for i in range(start, end):
    ports.put(i)  # push each port number into the thread-safe queue

# ===== Worker function executed by each thread =====
def scan():
    while not ports.empty():  # keep pulling ports until the queue is empty
        try:
            port = ports.get_nowait()  # get the next port without blocking
        except Exception:
            break  # queue became empty between the check and the get, so stop this worker

        try:
            r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a TCP socket
            r.settimeout(1.5)  # set a short timeout so scanning doesn't hang on filtered ports
            result = r.connect_ex((target_ip, port))  # attempt connection; returns 0 on success (port open)
            if result == 0:  # port is open
                try:
                    result_service = socket.getservbyport(port)  # try to resolve the common service name for this port
                except:
                    result_service = "unknwon"  # fallback if the port has no known service mapping

                console.print(
                    f"[bold green][+]FOUND: {port} : {result_service}"
                    f"{f' : ({result_server})' if args.server else ''}"
                    "[/bold green]"
                )  # print the open port, its service, and optionally the detected server header

                if args.outputJSON:  # if JSON output was requested, record this result as a dict
                    json_file.append({
                        "Port" : port,
                        "Service" : result_service,
                        "Server" : result_server,
                        "Status" : "open"
                    })
                if args.outputNORMAL:  # if plain text output was requested, record this result as a formatted string
                    normal_file.append(f"[+]FOUND: {port} : {result_service} : {result_server}")
            r.close()  # always close the socket after checking, whether open or not
        except (socket.timeout, ConnectionRefusedError, OSError):
            pass  # silently ignore closed/filtered ports or connection errors
        finally:
            ports.task_done()  # mark this port as processed regardless of outcome

# ===== Run the scan using a thread pool =====
try:
    with console.status("[bold cyan]Scanning ...[/bold cyan]"):  # show a spinner while scanning runs
        with ThreadPoolExecutor(max_workers=args.threads) as executor:  # create a pool of worker threads
            for _ in range(args.threads):
                executor.submit(scan)  # launch each worker thread running the scan() function
except KeyboardInterrupt:
    console.print("[bold red][!]Stopped bu user...[/bold red]")  # handle Ctrl+C gracefully
    os._exit(0)  # force-exit immediately since threads may still be running

# ===== Write results to output files if requested =====
if args.outputJSON:
    with open(args.outputJSON, "w") as f:
        json.dump(json_file, f, indent=4)  # save all collected results as a formatted JSON file

if args.outputNORMAL:
    with open(args.outputNORMAL, "w") as f:
        for line in normal_file:
            f.write(line + "\n")  # save all collected results as plain text lines

# ===== Done =====
console.print(Rule())  # print a closing separator line
console.print("[bold cyan][^_^] Scan completed successfully.[/bold cyan]")  # final success message
