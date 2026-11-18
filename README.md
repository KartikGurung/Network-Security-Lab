# NETWORK SECURITY LAB

<div align="center">

**A Python-based cybersecurity laboratory for cryptography, integrity, authentication, certificate, traffic, wireless, and secure communication analysis**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)](https://www.wireshark.org/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.kernel.org/)
[![OpenPGP](https://img.shields.io/badge/OpenPGP-4A4A4A?style=for-the-badge&logo=gnuprivacyguard&logoColor=white)](https://www.openpgp.org/)

</div>

> A hands-on academic repository demonstrating practical network security concepts through scripts, packet captures, screenshots, and technical procedures.

## Navigation

| [About](#about-this-repository) | [Objectives](#learning-objectives) | [Tools](#tools-and-technologies) | [Experiments](#laboratory-experiments) | [Structure](#repository-structure) | [Disclaimer](#ethical-use-disclaimer) |
|:---:|:---:|:---:|:---:|:---:|:---:|

---

## About This Repository

**Network Security Lab** is an academic collection of eight practical cybersecurity experiments. It combines Python implementations with industry-used security concepts and tools to demonstrate:

- Classical and modern cryptographic operations
- Data integrity and tamper detection
- Challenge-response authentication and replay detection
- X.509 certificate and public-key validation
- HTTP, TLS, SSH, and EAPOL network traffic analysis
- WPA2 four-way-handshake inspection
- End-to-end email security using OpenPGP

The repository is suitable for a network security course, technical portfolio, or guided laboratory study. Screenshots and packet captures document selected practical observations, while source files provide reproducible code examples.

## Learning Objectives

By working through this laboratory, students can develop skills in:

- Implementing Caesar and Vigenere transformations
- Computing and comparing SHA-256 hashes
- Understanding challenge-response authentication
- Identifying replay-based authentication weaknesses
- Validating certificate public keys and certificate integrity
- Inspecting HTTP, TLS, SSH, and 802.11 packet exchanges
- Parsing WPA2 EAPOL-Key frames and identifying handshake stages
- Using public-key cryptography for encryption and digital signatures
- Organizing cybersecurity evidence and laboratory documentation

---

## Tools and Technologies

| Category | Technology | Evidence of use |
|---|---|---|
| Programming | Python 3 | Python scripts across Experiments 1–4 and 7 |
| API framework | FastAPI | `/user` challenge-response prototype in Experiment 3 |
| Cryptography | `cryptography` package | X.509 parsing, public-key serialization, and certificate verification |
| Hashing | Python `hashlib` | SHA-256 integrity and challenge-response calculations |
| Web framework server | Uvicorn | Intended to serve the FastAPI prototype |
| Packet analysis | Wireshark | HTTP, TLS, and WPA2/EAPOL captures and screenshots |
| Packet parsing | Scapy | EAPOL and IEEE 802.11 packet parsing in Experiment 7 |
| Network protocol | SSH/OpenSSH | Secure shell session screenshots in Experiment 6 |
| Email security | Thunderbird with OpenPGP | Encrypted and digitally signed email in Experiment 8 |
| Operating systems | Kali Linux / Linux | Laboratory environment shown in repository screenshots |

### Python Dependencies

The repository contains no dependency manifest. Install the libraries explicitly used by the source code:

```bash
python -m pip install cryptography fastapi uvicorn scapy
```

> `hashlib`, `random`, `sys`, and `os` are standard Python modules and do not require installation.

---

## Laboratory Experiments

| No. | Experiment | Description | Technologies | Documentation |
|---:|---|---|---|---|
| 1 | [Classical Encryption Techniques](Experiment-1/) | Caesar cipher and Vigenere cipher encryption/decryption | Python | [Source](Experiment-1/exp-1.py) |
| 2 | [SHA-256 File Integrity](Experiment-2/) | Trusted hash creation and modification detection | Python, SHA-256 | [Source](Experiment-2/exp-2.py) · [Sample](Experiment-2/sample.txt) |
| 3 | [Challenge-Response Authentication](Experiment-3/) | Challenge generation, shared-secret hashing, and replay simulation | Python, hashlib, FastAPI | [Console demo](Experiment-3/exp-3.py) · [API prototype](Experiment-3/exp-3_improvement.py) |
| 4 | [X.509 Certificate Verification](Experiment-4/) | Certificate public-key matching and certificate hashing | Python, `cryptography`, OpenSSL-compatible PEM | [Source](Experiment-4/certificate_verify.py) · [Certificate](Experiment-4/certificate.crt) · [Screenshots](Experiment-4/Screenshots/) |
| 5 | [Wireshark Network Traffic Analysis](Experiment-5/) | HTTP and TLS traffic observation, packet detail, and handshake analysis | Wireshark, HTTP, TLS | [Screenshots](Experiment-5/) |
| 6 | [SSH Session Analysis](Experiment-6/) | Secure shell connection and remote command/session observation | Kali Linux, SSH/OpenSSH | [Screenshots](Experiment-6/) |
| 7 | [WPA2 Four-Way Handshake Analysis](Experiment-7/) | EAPOL-Key capture parsing and handshake message classification | Wireshark, Scapy, 802.11, WPA2 | [Analyzer](Experiment-7/wpa2_analyzer.py) · [Capture](Experiment-7/wpa2-four-way-handshake.pcap) |
| 8 | [PGP-Encrypted Email](Experiment-8/) | Thunderbird/OpenPGP key exchange, encryption, signing, and attachment security | Thunderbird, OpenPGP | [Full documentation](Experiment-8/README.md) · [Public keys](Experiment-8/Outputs/) |

---

## Experiment Documentation

<details open>
<summary><strong>1 — Classical Encryption Techniques</strong></summary>

- **Aim:** Demonstrate substitution and polyalphabetic cipher operations.
- **Concepts Covered:** Caesar shift, Vigenere key cycles, case preservation, and plaintext/ciphertext round trips.
- **Tools Required:** Python 3.
- **Implementation:** Run `Experiment-1/exp-1.py` and enter text and cipher parameters interactively.
- **Learning Outcome:** Understand basic transposition-free substitution and the weaknesses of classical ciphers.

</details>

<details>
<summary><strong>2 — SHA-256 File Integrity</strong></summary>

- **Aim:** Demonstrate how hashing can detect file modification.
- **Concepts Covered:** SHA-256 digests, trusted reference values, and tamper detection.
- **Tools Required:** Python 3 and `hashlib`.
- **Implementation:** Run `Experiment-2/exp-2.py`. The script writes a known value to `sample.txt`, records a hash, changes the file, recalculates the hash, and compares both values.
- **Learning Outcome:** Recognize the role of hashing in integrity verification.

</details>

<details>
<summary><strong>3 — Challenge-Response Authentication and Replay Attack</strong></summary>

- **Aim:** Explore challenge-response authentication and replay prevention.
- **Concepts Covered:** Shared secrets, SHA-256 responses, random challenges, and replay of a stale response.
- **Tools Required:** Python 3; FastAPI and Uvicorn for the API prototype.
- **Implementation:** Run `Experiment-3/exp-3.py` for the console demonstration. Run `uvicorn exp-3_improvement:app --reload` inside `Experiment-3` to start the API.
- **Learning Outcome:** Understand how fresh challenges can prevent reuse of old authentication responses.

</details>

<details>
<summary><strong>4 — X.509 Certificate Public-Key Verification</strong></summary>

- **Aim:** Confirm that a certificate contains the public key derived from the matching private key.
- **Concepts Covered:** X.509 certificates, PEM/DER encoding, public-key serialization, and SHA-256 integrity hashes.
- **Tools Required:** Python 3, `cryptography`, and a matching private key.
- **Implementation:** `certificate_verify.py` loads `certificate.crt` and `private.key`, serializes both public keys, compares SHA-256 values, and hashes the certificate file.
- **Learning Outcome:** Understand public-key/certificate association and basic certificate integrity verification.

</details>

<details>
<summary><strong>5 — Wireshark Network Traffic Analysis</strong></summary>

- **Aim:** Observe application and transport traffic using packet capture evidence.
- **Concepts Covered:** HTTP request/response exchange, encrypted TLS traffic, TCP sequencing, and packet dissection.
- **Tools Required:** Wireshark and a local packet-capture environment.
- **Implementation:** Inspect the five screenshots in `Experiment-5/` for HTTP, TCP, and TLS packet details.
- **Learning Outcome:** Interpret protocol metadata and distinguish plaintext application traffic from encrypted sessions.

</details>

<details>
<summary><strong>6 — SSH Session Analysis</strong></summary>

- **Aim:** Demonstrate a secure remote-shell session.
- **Concepts Covered:** SSH connection behavior, remote command execution, and warning indicators shown by the lab host.
- **Tools Required:** Kali Linux or a Linux environment with an OpenSSH client and an authorized SSH server.
- **Implementation:** Review the two captured screenshots in `Experiment-6/`.
- **Learning Outcome:** Understand basic SSH operational behavior and recognize the importance of host and user authentication.

</details>

<details>
<summary><strong>7 — WPA2 Four-Way Handshake Analysis</strong></summary>

- **Aim:** Analyze a captured WPA2 four-way-handshake exchange.
- **Concepts Covered:** EAPOL-Key frames, replay counters, ANonce/SNonce values, MIC fields, retransmissions, and handshake completeness.
- **Tools Required:** Python 3, Scapy, a WPA2 packet capture, and the supporting 802.11 environment.
- **Implementation:** Run `python wpa2_analyzer.py wpa2-four-way-handshake.pcap` inside `Experiment-7`.
- **Learning Outcome:** Identify handshake message variants and distinguish retransmitted frames from unique handshake frames.

</details>

<details>
<summary><strong>8 — PGP-Encrypted Email with Thunderbird</strong></summary>

- **Aim:** Exchange encrypted and digitally signed email using Thunderbird OpenPGP.
- **Concepts Covered:** Public/private key pairs, key fingerprints, confidentiality, authentication, digital signatures, and encrypted attachments.
- **Tools Required:** Mozilla Thunderbird, OpenPGP support, an authorized email account, and a communication partner.
- **Implementation:** Follow the procedures and evidence in [`Experiment-8/README.md`](Experiment-8/README.md).
- **Learning Outcome:** Understand key exchange and trust, message decryption, signature verification, and secure attachment sharing.

</details>

---

## Repository Structure

```text
Network-Security-Lab/
├── README.md
├── Experiment-1/
│   └── exp-1.py
├── Experiment-2/
│   ├── exp-2.py
│   └── sample.txt
├── Experiment-3/
│   ├── exp-3.py
│   └── exp-3_improvement.py
├── Experiment-4/
│   ├── .gitignore
│   ├── cert.cnf
│   ├── certificate.crt
│   ├── certificate_verify.py
│   └── Screenshots/
├── Experiment-5/
│   └── Screenshot_*.png
├── Experiment-6/
│   └── WhatsApp Image 2026-10-16 at 7.27.55 AM*.jpeg
├── Experiment-7/
│   ├── wpa2-four-way-handshake.pcap
│   ├── wpa2_analyzer.py
│   └── Screenshot_*.png
└── Experiment-8/
    ├── README.md
    └── Outputs/
        ├── Abhishek Sharma publickey.asc
        ├── Tanish Sharma publickey.asc
        └── ss1.png – ss8.png
```

### Repository Notes

- `Experiment-4/private.key` is not present in the repository and is intentionally excluded by `Experiment-4/.gitignore`. It must be supplied locally before `certificate_verify.py` can run.
- Experiments 5 and 6 currently contain laboratory screenshots but no source-code or procedure Markdown files.
- Experiment 8 includes the public keys used for the documented key exchange. Private key material is not included.
- No dependency manifest is currently provided for the complete repository.

---

## Learning Outcomes

Completion of these laboratories demonstrates practical familiarity with:

- Classical cipher operations and their limitations
- Cryptographic hashing and integrity monitoring
- Freshness, replay resistance, and authentication challenges
- Certificate parsing and public-key verification
- Network protocol analysis with Wireshark
- EAPOL/WPA2 capture interpretation
- SSH secure-session concepts
- Public-key encryption and digital-signature workflows
- Cybersecurity evidence collection and technical report structure

---

## References

- [Python Documentation](https://docs.python.org/3/)
- [Python `hashlib`](https://docs.python.org/3/library/hashlib.html)
- [Cryptography Project](https://cryptography.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Scapy Documentation](https://scapy.net/)
- [OpenSSH Documentation](https://www.openssh.com/manual.html)
- [Mozilla Thunderbird OpenPGP](https://support.mozilla.org/en-US/kb/thunderbird-openpgp-configuration)
- [OpenPGP Standard](https://www.openpgp.org/about/)
- [NIST SHA-2 Overview](https://csrc.nist.gov/publications/detail/fips/180/4/final)

---

## Ethical Use Disclaimer

This repository is for authorized academic, educational, and defensive use only. Perform security testing, packet capture, authentication experiments, wireless analysis, SSH access, and network inspection only on systems and networks you own or where you have explicit written authorization.

Use captured traffic and public/private key material responsibly. Do not intercept third-party communications, test production infrastructure without approval, or distribute private key material.

---

## Author / Maintainer

**Maintained for academic and practical cybersecurity laboratory purposes.**

Repository owner and contributor identity can be reviewed through the GitHub repository metadata.
