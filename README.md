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

## 🛠️ Technical Arsenal
**Languages & Tools utilized in this internship:**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## ⚠️ Disclaimer
All tools and scripts in this repository are developed strictly for **educational purposes** and legitimate security testing as part of an internship program. The detailed "Risk Reports" included in each folder demonstrate the defensive perspective of these tools.

---
*Licensed under the MIT License.*