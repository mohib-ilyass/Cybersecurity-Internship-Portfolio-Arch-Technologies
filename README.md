# 🛡️ Cybersecurity Internship Portfolio

> **Intern:** Mohib Ilyass
> **Role:** Cybersecurity Intern
> **University:** COMSATS University Islamabad (BS Cybersecurity)

## 📋 Overview
This repository serves as a centralized portfolio for the projects and technical tasks completed during my Cybersecurity Internship. The focus of these tasks is to bridge the gap between **theoretical concepts** (OSI Model, Encryption, Endpoint Security) and **practical implementation** using Python.

## 📂 Project Roadmap

### 1. [Task 1: NetProbe (Network Sniffer)](./Task1_NetworkSniffer)
**Objective:** Build a tool to analyze network traffic at the packet level.
* **Description:** A hybrid network sniffer that bypasses OS restrictions to capture Ethernet frames, IPv4 packets, TCP segments, and UDP datagrams. It manually dissects headers using bitwise operations to extract deep packet info.
* **Tech Stack:** Python, `scapy`, `struct`, `socket`.
* **Key Skills:**
    * ✅ OSI Layer Analysis (L2, L3, L4).
    * ✅ Raw Socket Programming.
    * ✅ Hexadecimal & ASCII Data Parsing.
* **[View Project ➜](./Task1_NetworkSniffer)**

---

### 2. [Task 2: KeyLogSim (Keylogger Simulation)](./Task2_Keylogger)
**Objective:** Simulate an endpoint attack to understand input interception risks.
* **Description:** A Proof-of-Concept (PoC) script that hooks into the Windows input chain to capture keystrokes. This project includes a detailed risk assessment report on how malware bypasses network encryption (HTTPS) by attacking the endpoint.
* **Tech Stack:** Python, `pynput`, Windows API.
* **Key Skills:**
    * ✅ Windows Hooks & API.
    * ✅ Endpoint Security Assessment.
    * ✅ Malware Behavior Analysis.
* **[View Project ➜](./Task2_Keylogger)**

---
### [Task-3] Data Recovery & Forensics
**Objective:** Simulate data loss and attempt retrieval using forensic tools.
* **Tools Used:** Recuva, TestDisk, USB Storage (FAT32).
* **Description:**
    * Simulated accidental data deletion (`Shift+Delete`) on a FAT32 drive.
    * Successfully recovered text, image, and spreadsheet files.
    * Documented the difference between file system "deletion" vs. physical overwriting.

### [Task-4] Credit Card Fraud Detection
**Objective:** Build an AI model to detect fraudulent transactions.
* **Tools Used:** Python, Scikit-Learn, Pandas, Random Forest, SMOTE.
* **Description:**
    * Analyzed a dataset of 284,000+ credit card transactions.
    * Solved the "Class Imbalance" problem (0.17% fraud rate) using SMOTE (Synthetic Minority Over-sampling Technique).
    * Achieved a **Recall rate of ~86%**, effectively catching fraudulent activity while minimizing false alarms.
## 🛠️ Technical Arsenal
**Languages & Tools utilized in this internship:**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![TestDisk](https://img.shields.io/badge/TestDisk-000000?style=for-the-badge&logo=linux&logoColor=white)
![Recuva](https://img.shields.io/badge/Recuva-58D68D?style=for-the-badge&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---
## ⚠️ Disclaimer
All tools and scripts in this repository are developed strictly for **educational purposes** and legitimate security testing as part of an internship program. The detailed "Risk Reports" included in each folder demonstrate the defensive perspective of these tools.

---
*Licensed under the MIT License.*
