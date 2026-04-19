# Python OOP Banner Grabber

## Description
A lightweight, Object-Oriented Python script designed for network reconnaissance. It connects to a specified target IP and a list of ports, retrieves the service banners (software versions, OS details), and securely handles network errors. The tool also features a reporting mechanism that logs the discovered banners into a text file.

## Features
* **Object-Oriented Design:** Clean and modular class structure (`BannerGrabber`).
* **Advanced Error Handling:** Gracefully handles `ConnectionRefusedError`, `socket.timeout`, and `KeyboardInterrupt` without crashing.
* **File I/O Logging:** Automatically saves the scan results to a local `.txt` file for further vulnerability analysis.
* **Ethical Hacking Ready:** Designed for authorized Penetration Testing environments.

## Usage
Modify the `target_ip` and `port_list` variables within the script to point to your authorized target, then execute the script via terminal:

```bash
python3 main.py