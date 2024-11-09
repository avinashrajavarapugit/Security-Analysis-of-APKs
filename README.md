# Security Analysis of APKs

This project performs malware detection on Android APKs by reverse engineering, analyzing opcodes and permissions, and identifying malicious patterns.

## Features

- **Opcode Analysis**: Uses Androguard to examine bytecode instructions, identifying obfuscation and malicious patterns.
- **Permission Analysis**: Checks permissions for unusual or excessive requests, often indicative of malware.
- **Malware Detection**: Matches opcodes and permissions against known malware signatures.

## Tech Stack

- **Python**
- **Androguard**: For reverse engineering and APK analysis
- **Django & Jinja2** (optional): For creating a frontend if needed
- **Linux**: Primary environment for analysis

## Existing
![image](https://github.com/user-attachments/assets/48f67ea7-e011-4061-86d7-5b67092d85dd)

## Proposed System
![image](https://github.com/user-attachments/assets/a9a2f43e-6b07-451f-8e59-809a06393ac7)

## Malware detection website

![image](https://github.com/user-attachments/assets/19fae14b-5dc9-4e5a-89f0-3e0c2ebbf1f6)

![image](https://github.com/user-attachments/assets/770afa1e-8455-4c41-b8d0-7005f7830455)

![image](https://github.com/user-attachments/assets/7c7b727c-d0c3-4b95-ae88-3904f237d384)

![image](https://github.com/user-attachments/assets/7b6566af-2bb8-4184-a84c-56cff17a3d3b)

##ROC CURVES

![image](https://github.com/user-attachments/assets/bd8048a7-2bbc-4da2-98b4-fdff8f4e2583)
