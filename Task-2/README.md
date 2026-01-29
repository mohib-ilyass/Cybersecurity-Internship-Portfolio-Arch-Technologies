# Educational Keylogger Simulation ⌨️

**Task ID:** Task-2  
**Domain:** Malware Analysis / Endpoint Security  
**Language:** Python  

---

## 📝 Project Overview
This project is a basic **Keylogger** developed to demonstrate how malicious software captures keystrokes on a target system. The tool runs in the background, intercepting keyboard inputs via the `pynput` library and logging them to a local text file in real-time.

**⚠️ Ethical Disclaimer:** This tool was created strictly for **educational purposes** to understand the mechanics of spyware and endpoint threats. It should **never** be used on a system without the owner's explicit permission. Unauthorized use of keyloggers is illegal and unethical.

---

## ⚙️ How It Works
1. **Library:** Uses the `pynput` library to control and monitor input devices.
2. **Interception:** The script creates a "Listener" object that waits for keyboard events.
3. **Logging:**
    * **Alphanumeric keys** are logged directly.
    * **Special keys** (Space, Enter, Shift) are formatted for readability (e.g., `[ENTER]`).
4. **Termination:** The logging loop stops safely when the `ESC` key is pressed.

---

## 🚀 Installation & Usage

### 1. Install Dependencies
You need the `pynput` library to interact with the keyboard.
```bash
pip install pynput
