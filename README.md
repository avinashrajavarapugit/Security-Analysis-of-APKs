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

