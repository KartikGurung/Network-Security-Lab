# Lab 02: Cryptographic Hashing & Data Integrity

## Overview
This module demonstrates cryptographic data integrity verification using the **Secure Hash Algorithm 256-bit (SHA-256)**. By establishing a trusted baseline digest and introducing targeted modifications to a payload, this lab illustrates the **avalanche effect** and the role of one-way hash functions in tamper detection.

---

## Technical Specifications

| Parameter | Specification |
| :--- | :--- |
| **Algorithm** | SHA-256 (NIST FIPS 180-4) |
| **Digest Length** | 256 bits (64 hexadecimal characters) |
| **Security Attributes** | Pre-image resistance, Second pre-image resistance, Collision resistance |
| **File Analyzed** | `sample.txt` |
| **Primary Script** | `exp-2.py` |
| **Dependencies** | Python `hashlib` (standard library) |

---

## Technical Workflow

```
┌────────────────────────┐       SHA-256
│ Initial 'sample.txt'   │ ───────────────────> Trusted Reference Hash: H_0
└────────────────────────┘
            │
      [1-byte edit]
            │
            ▼
┌────────────────────────┐       SHA-256
│ Modified 'sample.txt'  │ ───────────────────> New Computed Hash: H_1
└────────────────────────┘
            │
            ▼
    Compare (H_0 == H_1) ────> Result: "Data has been Modified" (Tamper Detected)
```

---

## Verification Pipeline

1. **Baseline Generation:** The script populates `sample.txt` with an initial string:
   ```text
   This is my intgrity test.
   ```
   A 256-bit SHA-256 digest is generated and captured as the trusted reference state.

2. **Tamper Simulation:** A subtle alteration is introduced (spelling adjustment and case mutation):
   ```text
   This is my integrity Test!
   ```

3. **Integrity Evaluation:** The digest is recomputed over the mutated file buffer and evaluated against the trusted hash. Any deviation triggers an immediate integrity alarm.

---

## Execution Guide

### Running the Verification Script
```bash
python exp-2.py
```

### Observed Terminal Output
```text
Trusted SHA-256: 4e9c7da7940156d95392cf99a19d9b68a8dc4e9c4033b0be226e63dfcae3a84b
New SHA-256:     934b92c48d1e8ef9fa483d31ca92209d8d6411d51c33f81e3f8a0ff1ef726a4a
Data has been Modified
```

---

## Security Takeaways
- **The Avalanche Effect:** Changing even a single bit or character in the input string yields a totally uncorrelated, pseudo-random digest across the 256-bit output space.
- **Verification Integrity:** Hash digests are deterministic; identically sized files with identical byte sequences will always produce identical digests under the same hash function.
- **Defensive Role:** Cryptographic checksums serve as the core primitive for package integrity verification, digital forensics chain-of-custody tracking, and git commit hashing.
