# Lab 01: Classical Encryption Techniques

## Overview
This module explores classical cryptographic mechanisms through Python implementations of the **Caesar Cipher** (monoalphabetic substitution) and the **Vigenère Cipher** (polyalphabetic substitution). These foundational ciphers illustrate mathematical transformations over finite alphabets and highlight why basic substitution is insufficient for modern information security.

---

## Technical Specifications

| Parameter | Caesar Cipher | Vigenère Cipher |
| :--- | :--- | :--- |
| **Cipher Class** | Monoalphabetic Substitution | Polyalphabetic Substitution |
| **Key Type** | Integer shift value ($k \in [0, 25]$) | Keyword string ($K \in \Sigma^+$) |
| **Mathematical Domain** | $\mathbb{Z}_{26}$ modular arithmetic | $\mathbb{Z}_{26}$ modular addition per character |
| **Vulnerability** | Frequency analysis, brute-force ($26$ keys) | Kasiski examination, Index of Coincidence |
| **Primary Script** | `exp-1.py` | `exp-1.py` |

---

## Cryptographic Mechanics

### 1. Caesar Cipher
The transformation maps each plaintext character $p$ to ciphertext character $c$ using a modular shift $k$:

$$E(p) = (p + k) \pmod{26}$$
$$D(c) = (c - k) \pmod{26}$$

The implementation preserves case sensitivity (`isupper()` / `islower()`) while non-alphabetic symbols pass through unaltered.

### 2. Vigenère Cipher
The Vigenère cipher mitigates single-alphabet frequency distribution by cycling a keyword of length $m$:

$$c_i = (p_i + k_{i \pmod m}) \pmod{26}$$
$$p_i = (c_i - k_{i \pmod m}) \pmod{26}$$

---

## Execution Guide

### Prerequisites
Python 3.8+ (standard library only; no external dependencies required).

### Running the Script
```bash
python exp-1.py
```

### Sample Interactive Session
```text
Enter the text: DefensiveSecurity
Enter the number of shift: 3
Ciphertext = GhihqvlyhVhfxulwb
Plaintext = DefensiveSecurity

Enter the text: ConfidentialMessage
Enter your key to encrypt: CIPHER
Ciphertext = ErdubfxkxbcsThvheoi
Plaintext = ConfidentialMessage
```

---

## Security Analysis & Weaknesses

```
[Plaintext Distribution] ──> [Monoalphabetic Shift] ──> [Preserved Frequency Profile]
                                                            │
                                                            └──> Vulnerable to statistical cryptanalysis
```

1. **Trivial Key Space (Caesar):** With only 25 non-trivial shift permutations, brute-force recovery requires less than a millisecond on modern processors.
2. **Periodic Leakage (Vigenère):** Although it flattens simple unigram histograms, repetitive patterns in natural language leak the keyword length $m$ (exploitable via the Kasiski test), allowing cryptanalysts to partition the ciphertext into $m$ independent Caesar ciphers.

---

## Learning Verification
- Verified bi-directional symmetry (plaintext $\rightarrow$ ciphertext $\rightarrow$ plaintext).
- Observed preservation of capitalization and punctuation boundaries.
- Confirmed that security in modern systems requires computational indistinguishability, high diffusion, and confusion (Shannon's principles) rather than modular character rotation.
