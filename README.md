<p align="center">
  <h1 align="center">🦅 Ncrow - Multi-Threaded Port Scanner 🦅</h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT%20%2B%20Custom-blue?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/languages/top/BlackCrow-Code/Ncrow?style=for-the-badge&color=green" alt="Python">
  <img src="https://img.shields.io/github/stars/BlackCrow-Code/Ncrow?style=for-the-badge&color=gold" alt="Stars">
  <img src="https://img.shields.io/badge/version-4.0.0-red?style=for-the-badge" alt="Version">
</p>

<p align="center">
  <b>A fast, lightweight, and modern multi-threaded port scanner built with Python and Sockets, for Cyber Security professionals.</b>
</p>

---

## 🚀 Features

* ⚡ **Extreme Speed:** Leverages a `ThreadPoolExecutor` with a thread-safe `Queue` to scan hundreds of ports concurrently (up to 300 threads).
* 🎨 **Color-Coded Output:** Beautiful terminal output powered by `rich`, with distinct colors for open ports and services.
* 🔍 **Service Grabbing:** Automatically detects the underlying service running on open ports.
* 🌐 **Server Detection:** Grabs the HTTP `Server` header from the target when available.
* 🧠 **Smart Target Parsing:** Accepts both raw IPs and full URLs, automatically extracting the hostname.
* 💾 **Export Results:** Save scan results as `JSON` or plain text files for later reporting.
* 🛑 **Graceful Interrupt Handling:** Stop a scan cleanly at any time with `Ctrl+C`.
* 🛡️ **Clean CLI:** Built using `argparse` for a professional command-line interface experience.

---

## 📦 Requirements

* Python 3.x
* Kali Linux (or any Linux distro with Python 3 installed)
* Dependencies listed in `requirements.txt` (`rich`, `pyfiglet`, `requests`)

---

## 🛠️ Installation

Run the following commands in your Kali Linux terminal to install and setup Ncrow:

```bash
# Clone the repository
git clone https://github.com/BlackCrow-Code/Ncrow.git

# Navigate to the tool directory
cd Ncrow

# Install dependencies
pip install -r requirements.txt
```

---

## 💻 Usage & Options

To view the help menu and understand the arguments, use the `-h` or `--help` flag:

### 📄 Help Menu

```text
usage: Ncrow.py [-h] -t TARGET [-p PORT PORT] [-a] [-T THREADS] [-s]
                 [-oj OUTPUTJSON] [-on OUTPUTNORMAL]

Ncrow-PortScanner

options:
  -h, --help            show this help message and exit
  -t, --target TARGET   Url or IP_Address
  -p, --port PORT PORT  Start with port [Space] finish with port
  -a, --all             Scan all ports
  -T, --threads THREADS Number of threads 300 limit
  -s, --server          Server INF
  -oj, --outputJSON     Save discovered ports to a (JSON) file
  -on, --outputNORMAL   Save discovered ports to a (NORMAL) file
```

### 🔍 Scan Examples

Scan a target for ports ranging from 1 to 1024:

```bash
sudo python3 ncrow.py -t <target> -p 1 1024
```

Scan all 65,535 ports with 200 threads and grab the server header:

```bash
sudo python3 ncrow.py -t <target> -a -T 200 -s
```

Scan and export results to both JSON and plain text files:

```bash
sudo python3 ncrow.py -t <target> -p 1 1024 -oj results.json -on results.txt
```

---

## 📸 Screenshots

<p align="center">

  # Help Menu

  <img width="647" height="364" alt="Help Menu" src="https://github.com/user-attachments/assets/0d680c1a-f73e-4113-b667-db96ca675cd4" />

  # Scan Example

  <img width="651" height="336" alt="Scan Example" src="https://github.com/user-attachments/assets/bd2ddb87-8124-42f7-99f9-08f2c96341ff" />

  # Interrupt Handling

  <img width="651" height="336" alt="Interrupt Handling" src="https://github.com/user-attachments/assets/5903e064-b132-445c-9661-c1a51df4a088" />

</p>

---

## ⚠️ Disclaimer

Ncrow is developed strictly for **educational and authorized security testing purposes only**.
Do not use this tool against any target without explicit permission from the owner.
The author is not responsible for any misuse or damage caused by this tool.

---

## 👤 Author

**BlackCrow-Code** — Security Researcher

---

## 📜 License

This project is licensed under the MIT License with Additional Custom Developer Terms.
Please review the full license text below - see the [LICENSE](LICENSE) file for details.
