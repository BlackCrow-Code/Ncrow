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
# Help Menu ![Help]
 <img width="791" height="329" alt="Screenshot From 2026-06-22 09-51-57" src="https://github.com/user-attachments/assets/50e92164-2329-415e-80e9-6d4991cf6fad" />


# Scan Example ![Scan] 
<img width="803" height="162" alt="normal (Edited)" src="https://github.com/user-attachments/assets/1bcccbfe-fed1-4a35-9ee8-ace60f938699" />


# Interrupt Handling ![Ctr+C] 
<img width="807" height="165" alt="Screenshot From 2026-06-22 09-51-35" src="https://github.com/user-attachments/assets/43d54972-6a12-4e36-ac6c-fd67052df350" />



## 📦 Requirements
Python 3.x — Kali Linux (recommended)

## 🚀 Usage


-Scan default ports (1-1024)

python ncrow.py -t <target>

-Scan all ports

python ncrow.py -t <target> -a

-Scan specific range

python ncrow.py -t <target> -p 1 8080

-With banner grabbing

python ncrow.py -t <target> -b

-Set thread count

python ncrow.py -t <target> -T 500

## ⚠️ Disclaimer
This tool is for **educational purposes** and **authorized testing only**.
The developer is not responsible for any misuse.

## 👤 Author
**BlackCrow-Code** — Security Researcher & Programmer & cybersecurity engineer
