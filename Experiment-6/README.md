# Lab 06: Secure Shell (SSH) Protocol Analysis & Remote Administration

## Overview
This laboratory examines the **Secure Shell (SSH)** protocol for encrypted remote administration. Executed within an isolated penetration testing network, an OpenSSH client running on **Kali Linux** initiates an encrypted terminal session to an audit target (**Metasploitable 2**), demonstrating session establishment, host key negotiation, and secure remote execution.

---

## Technical Specifications

| Parameter | Specification |
| :--- | :--- |
| **Client Environment** | Kali Linux (`kali@kali`) |
| **Server Environment** | Metasploitable 2 (`Linux metasploitable 2.6.24-16-server`) |
| **Network Target** | `192.168.148.128:22/TCP` |
| **Protocol** | SSH-2.0 (OpenSSH) |
| **Key Algorithm Flag** | `-o HostKeyAlgorithms=+ssh-rsa` (Enabling legacy host-key compatibility) |
| **Security Mechanism** | Asymmetric host verification, symmetric session encryption, MAC integrity |
| **Artifacts** | 2 Photographic Evidence Captures |

---

## Protocol Lifecycle & Threat Analysis

```
Kali Linux Client                                  Metasploitable Target
(192.168.148.130)                                    (192.168.148.128)
        │                                                    │
        │ ─── 1. TCP Handshake (Port 22) ──────────────────> │
        │ <── 2. Protocol Identification (SSH-2.0) ───────── │
        │                                                    │
        │ <── 3. Key Exchange & Server Host Key (RSA) ────── │
        │ [Verify Host Key Fingerprint against known_hosts]  │
        │                                                    │
        │ <== 4. Diffie-Hellman Shared Secret Derived =====> │
        │     (Symmetric Channel Encryption Initiated)       │
        │                                                    │
        │ ─── 5. Authenticate: Password / Public Key ──────> │
        │ <── 6. Remote PTY Session Granted ──────────────── │
```

---

## Laboratory Procedure & Execution

### 1. Initiating the Secure Connection
Because legacy target distributions may not advertise modern Ed25519 or ECDSA algorithms by default, the client explicitly negotiates RSA compatibility:

```bash
ssh -o HostKeyAlgorithms=+ssh-rsa msfadmin@192.168.148.128
```

#### Terminal Observations:
- **Post-Quantum Warning:** The modern OpenSSH client alerts the user:
  ```text
  ** WARNING: connection is not using a post-quantum key exchange algorithm.
  ** This session may be vulnerable to "store now, decrypt later" attacks.
  ```
- **Session Authentication:** Upon entering valid credentials, the user is admitted to `msfadmin@metasploitable:~$`.

### 2. Remote Command Execution
An encrypted test directory and file are constructed over the secure channel:
```bash
mkdir ssh-lab
cd ssh-lab
echo "Hello from my SSH session" > notes.txt
cat notes.txt
```

---

## Visual Evidence & Forensic Observations

### Evidence 1: Encrypted Session Initiation & Command Execution
Kali Linux terminal shows SSH connection initialization, post-quantum migration warning, and successful command execution on the target server.
![Kali Linux SSH Session](WhatsApp%20Image%202026-10-16%20at%207.27.55%20AM.jpeg)

### Evidence 2: Target Console Verification
Metasploitable host virtual console verifies that files created remotely through the SSH session (`ssh-lab/notes.txt`) exist in the target filesystem.
![Metasploitable Host Verification](WhatsApp%20Image%202026-10-16%20at%207.27.55%20AM(1).jpeg)

---

## Defensive Engineering Insights
1. **Rejection of Cleartext Protocols:** SSH completely replaces unencrypted administrative channels (Telnet, rlogin, rsh), ensuring password hashes and interactive commands cannot be captured passively.
2. **Host Authentication Integrity:** The SSH `known_hosts` mechanism stores server public keys upon first contact (TOFU - Trust On First Use) and raises critical warnings if host keys change, protecting against Man-in-the-Middle (MitM) attacks.
3. **Future-Proofing against SNDL:** The observed OpenSSH warning highlights emerging cybersecurity standards addressing "Store Now, Decrypt Later" (SNDL) threats, where adversaries capture encrypted traffic to decrypt later using quantum computers.
