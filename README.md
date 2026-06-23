<p align="center">
  <h1 align="center">🦅 Ncrow - Multi-Threaded Port Scanner 🦅</h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT%20%2B%20Custom-blue?style=for-the-badge" alt="License">

  <img src="https://img.shields.io/github/languages/top/BlackCrow-Code/Ncrow?style=for-the-badge&color=green" alt="Python">
  <img src="https://img.shields.io/github/stars/BlackCrow-Code/Ncrow?style=for-the-badge&color=gold" alt="Stars">
</p>

<p align="center">
  <b>A fast, lightweight, and modern multi-threaded port scanner built with Python, Sockets,  for Cyber Security professionals.</b>
</p>

---

## 🚀 Features
* ⚡ **Extreme Speed:** Leverages Python `threading` and `Semaphores` to scan hundreds of ports concurrently.
* 🎨 **Color-Coded Output:** Beautiful terminal output with distinct colors for open ports and services.
* 🔍 **Service Grabbing:** Automatically detects the underlying service running on open ports.
* 🛡️ **Stealth & Clean CLI:** Built using `argparse` for a professional command-line interface experience.

---

## 🛠️ Installation

Run the following commands in your Kali Linux terminal to install and setup Ncrow:

```bash
# Clone the repository
git clone [https://github.com/BlackCrow-Code/Ncrow.git](https://github.com/BlackCrow-Code/Ncrow.git)

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
usage: Ncrow.py [-h] -t TARGET [-p PORT PORT] [-a] [-T THREADS] [-b]

Ncrow-PortScanner

options:
  -h, --help            show this help message and exit
  -t, --target TARGET   Url or IP_Address
  -p, --port PORT PORT  Start with port [Space] finish with port
  -a, --all             Scan all ports
  -T, --threads THREADS Number of threads
  -b, --banner          Banner Grabbing
```

### 🔍 Scan Example
To scan a target IP address for ports ranging from 1 to 1024, execute with root privileges:

```bash
sudo python3 ncrow.py -t <target> -p 1 1024
```

---

## 📸 Screenshots
<p align="center">
  
  # Help Menu
  
  <img width="791" height="329" alt="Screenshot From 2026-06-22 09-51-57" src="https://github.com/user-attachments/assets/1f114fe5-ae3f-4376-ac4d-d89853965792" />
  
  # Scan Example
  
  <img width="803" height="162" alt="normal (Edited)" src="https://github.com/user-attachments/assets/cfe87dac-a85f-4a9b-9679-fd61c895542f" />
  
  # Interrupt Handling
  
  <img width="807" height="165" alt="Screenshot From 2026-06-22 09-51-35" src="https://github.com/user-attachments/assets/6d020596-bb56-4844-9fed-c049420e088c" />



  </p>

---

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
 
