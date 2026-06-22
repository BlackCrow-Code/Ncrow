# 🦅 Ncrow - Port Scanner

> See what's hiding behind every open port.

A fast and lightweight port scanner built in Python with multi-threading and banner grabbing support. Built on Kali Linux.

## ⚡ Features
- Multi-threaded scanning (fast)
- Banner grabbing to detect services
- Color-coded terminal output
- Scan specific port range or all 65535 ports
- Simple CLI interface
##Screenshots
--> Help Menu ![Help] <img width="791" height="329" alt="Screenshot From 2026-06-22 09-51-57" src="https://github.com/user-attachments/assets/3ccd4d41-4333-4d98-b217-fc5177de35ba" />

--> Scan Example ![Scan] <img width="803" height="162" alt="normal (Edited)" src="https://github.com/user-attachments/assets/04fbff4b-a006-4837-b4b8-d19e9a1e4fee" />

-->Interrupt Handling ![Ctr+C] <img width="807" height="165" alt="Screenshot From 2026-06-22 09-51-35" src="https://github.com/user-attachments/assets/96715f9d-1f97-480a-ad48-1944bc583d30" />


## 📦 Requirements
Python 3.x — Kali Linux (recommended)

## 🚀 Usage


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

## ⚠️ Disclaimer
This tool is for **educational purposes** and **authorized testing only**.
The developer is not responsible for any misuse.

## 👤 Author
**BlackCrow-Code** — Security Researcher & Programmer & cybersecurity engineer
