# 🦅 Ncrow - Port Scanner

> See what's hiding behind every open port.

A fast and lightweight port scanner built in Python with multi-threading and banner grabbing support. Built on Kali Linux.

## ⚡ Features
- Multi-threaded scanning (fast)
- Banner grabbing to detect services
- Color-coded terminal output
- Scan specific port range or all 65535 ports
- Simple CLI interface

## 📦 Requirements
Python 3.x — Kali Linux (recommended)

## 🚀 Usage

```bash
# Scan default ports (1-1024)
python ncrow.py -t <target>

# Scan all ports
python ncrow.py -t <target> -a

# Scan specific range
python ncrow.py -t <target> -p 1 8080

# With banner grabbing
python ncrow.py -t <target> -b

# Set thread count
python ncrow.py -t <target> -T 500
```

## ⚠️ Disclaimer
This tool is for **educational purposes** and **authorized testing only**.
The developer is not responsible for any misuse.

## 👤 Author
**BlackCrow-Code** — Security Researcher & Network Analyst
