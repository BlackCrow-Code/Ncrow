import socket
import threading
import argparse
from concurrent.futures import ThreadPoolExecutor
import os

# -----> CLI Arguments - Control the tool from terminal
parser = argparse.ArgumentParser(description="Ncrow-PortScanner")
parser.add_argument("-t", "--target", required=True, help="Url or IP_Address")
parser.add_argument("-p", "--port", nargs=2, type=int, default=[1, 1024], help="Start with port [Space] finish with port")
parser.add_argument("-a", "--all", action="store_true", help="Scan all ports")
parser.add_argument("-T", "--threads", default=200, type=int, help="Number of threads")
parser.add_argument("-b", "--banner", action="store_true", help="Bannre Grabbing")
args = parser.parse_args()

# -----> Target - Get the target from user input
target = args.target

# -----> Port Range - Set the port range to scan
if args.all:
    # Scan all possible ports
    start, end = 1, 65535
else:
    # Scan user-defined range (default: 1-1024)
    start, end = args.port[0], args.port[1]

# -----> Colors - Terminal color codes for output
RED = "\033[91m"
GREEN = "\033[92m"
REST = "\033[0m"
CYR = "\033[96m"

print("[!]Start Scanning...\n---------------------")

def scan(port):
    # Create a new TCP socket for each port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set timeout to avoid hanging on closed ports
    s.settimeout(0.5)
    
    # Try to connect - returns 0 if port is open
    result = s.connect_ex((target, port))
    
    if result == 0:
        # -----> Get Service Name
        try:
            service = socket.getservbyport(port)
        except:
            service = "unknown"

        banner = ""
        
        # -----> Banner Grabbing - Get service info if -b flag is used
        if args.banner:
            try:
                # Send HTTP request to grab banner
                s.send(b"HEAD/HTTP/1.0\r\n\r\n")
                banner = s.recv(1024).decode(errors="ignore").strip()
                
                # Extract Server header if available
                if "Server:" in banner:
                    for line in banner.split("\n"):
                        if "Server:" in line:
                            banner = line.strip()
                            break
                else:
                    # Take first 50 chars of first line
                    banner = banner.split("\n")[0][:50]
            except:
                banner = "No banner"

        # -----> Print Results
        if banner:
            # Print port with banner info
            print(f"[*]Open port {GREEN}{port}{REST}|{GREEN}{service}{REST}:[{GREEN}{banner}{REST}]...")
        else:
            # Print port without banner
            print(f"[*]Open port {GREEN}{port}{REST}|{GREEN}{service}{REST}...")

        s.close()

# -----> Thread Pool - Run scan() on all ports using multiple threads
try:
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(scan, range(start, end + 1))
except:
    # Handle Ctrl+C or user interrupt
    print(F"\n{RED}[!]Scan stoped by user..{REST}")
    os._exit(0)

print("---------------------\n[!]Fhinshed scaneing..")
