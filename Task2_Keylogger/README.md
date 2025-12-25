# ⌨️ KeyLogSim: Educational Keylogger Simulation

**A Python-based input capture tool developed for Cybersecurity Internship Task 2.**

## 📋 Overview
KeyLogSim is a "Proof of Concept" script designed to demonstrate how keystroke logging works within the Windows environment. It utilizes the `pynput` library to hook into keyboard events, capturing user input in real-time.

This project was built to analyze the mechanics of **Endpoint Input Capture** and understand why relying solely on network-layer encryption (HTTPS) is insufficient for data protection.

## ✨ Features
* **Global Hooking:** Captures keystrokes even when the script is running in the background.
* **Special Key Handling:** Correctly formats keys like `[ENTER]`, `[SPACE]`, and `[SHIFT]` for readability.
* **Safe Termination:** Includes a programmed "Kill Switch" (`ESC` key) for safe and easy testing.
* **File Logging:** Appends captured data immediately to a local text file.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Library:** `pynput` (Python Input)
* **Mechanisms:** Windows Hooks (`SetWindowsHookEx` wrapper), File I/O.

## 🚀 Installation & Usage

### Prerequisites
1.  Python 3.x installed.
2.  Install the required library:
    ```bash
    pip install pynput
    ```

### Running the Simulation
1.  Clone the repository.
2.  Run the script:
    ```bash
    python keylogger_sim.py
    ```
3.  Type anywhere on your system (Notepad, Browser, etc.).
4.  **Press `ESC` to stop the logger.**
5.  View the captured keystrokes in `key_log.txt`.

## ⚠️ Legal & Ethical Disclaimer
**For Educational Purposes Only.**
This script is developed strictly for academic research and cybersecurity training. It is designed to run visibly with a manual exit trigger. Unauthorized installation of keyloggers on devices you do not own is illegal and a violation of privacy laws.

## 📄 License
This project is licensed under the MIT License.