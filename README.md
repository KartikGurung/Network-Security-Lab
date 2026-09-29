# Network Security Lab Experiments

This repository contains a collection of Python-based security experiments covering classical cryptography, hashing, authentication, and X.509 certificate verification.

## Project Structure

- Experiment-1/exp-1.py — Caesar cipher and Vigenere cipher demonstration
- Experiment-2/exp-2.py — SHA-256 integrity check and tamper detection
- Experiment-2/sample.txt — sample text file used for hashing demonstration
- Experiment-3/exp-3.py — challenge-response authentication and replay attack example
- Experiment-3/exp-3_improvement.py — FastAPI-based challenge-response prototype
- X509-Self-Signed-Certificate

## Experiment Overview

### 1. Classical Encryption Techniques
The script in Experiment-1 demonstrates:
- Caesar cipher encryption and decryption
- Vigenere cipher encryption and decryption

Run it with:

```bash
cd Experiment-1
python3 exp-1.py
```

### 2. Data Integrity with Hashing
The script in Experiment-2 shows how SHA-256 helps detect tampering:
- create an initial trusted hash for a file
- modify the file content
- recalculate the hash and compare it with the original

Run it with:

```bash
cd Experiment-2
python3 exp-2.py
```

### 3. Authentication and Replay Attack
The script in Experiment-3 demonstrates:
- challenge-response authentication using a shared secret
- replay attack detection by comparing a stored response against a new challenge

Run it with:

```bash
cd Experiment-3
python3 exp-3.py
```

### 4. X.509 Certificate Verification
The X.509 certificate example validates that the public key contained in a certificate matches the public key derived from the private key. It also prints the SHA-256 hash of the certificate for integrity tracking.

Run it with:

```bash
cd "X509-Self-Signed-Certificate"
python3 certificate_verify.py
```

## Prerequisites

- Python 3.8 or later
- pip
- cryptography package
- fastapi and uvicorn for the API-based improvement example

Install the required dependencies with:

```bash
pip install cryptography fastapi uvicorn
```

## Learning Objectives

This lab is designed to help understand:
- symmetric encryption techniques
- hashing and file integrity verification
- authentication mechanisms using challenge-response patterns
- replay attack prevention
- X.509 certificate and public key validation

## Notes

These scripts are intended for academic and demonstration purposes in a network security or cybersecurity lab environment. They provide a hands-on introduction to security concepts and can be used as a foundation for further study into modern cryptographic systems.
