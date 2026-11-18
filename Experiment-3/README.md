# Lab 03: Challenge-Response Authentication & Replay Attack Defense

## Overview
This laboratory implements and evaluates **Challenge-Response Authentication** protocols to mitigate credential sniffing and replay attacks. It includes both a command-line simulation demonstrating the failure of replayed credentials against cryptographic nonces, and a FastAPI-driven REST API service prototype.

---

## Technical Specifications

| Parameter | Console Implementation (`exp-3.py`) | REST API Implementation (`exp-3_improvement.py`) |
| :--- | :--- | :--- |
| **Authentication Model**| Symmetric Shared-Secret Challenge-Response | RESTful Nonce Tokenization & Digest Verification |
| **Challenge Primitive** | Dynamic Cryptographic Nonce (`random.randint`) | Ephemeral 16-bit Nonce + Secret Salt |
| **Digest Function**     | SHA-256 (`hashlib`) | SHA-256 (`hashlib.sha256`) |
| **Attack Vector Tested**| Intercepted Credential Replay | Replay Invalidation |
| **Framework**           | Python Standard Library | FastAPI + Uvicorn ASGI Server |

---

## Protocol Architecture & Attack Model

### 1. Legitimate Authentication Exchange
```
Client (Has S)                                       Server (Has S)
   │                                                     │
   │ <─── 1. Generate Nonce Challenge (C_1) ──────────── │
   │                                                     │
   │ ─── 2. Compute Response: R_1 = SHA256(C_1 || S) ──> │
   │                                                     │
   │                                           [Verify R_1 == Expected]
   │ <─── 3. Access Granted ──────────────────────────── │
```

### 2. Replay Attack Invalidation
```
Attacker (Intercepted R_1)                           Server (Has S)
   │                                                     │
   │ <─── 1. Generate Fresh Challenge (C_2) ─────────── │
   │                                                     │
   │ ─── 2. Replay Stale Response R_1 ─────────────────> │
   │                                                     │
   │                                           [Compute Expected: SHA256(C_2 || S)]
   │                                           [Compare: R_1 != Expected]
   │ <─── 3. Replay Attack Blocked! ─────────────────── │
```

---

## Code Implementations

### A. Console Demonstration (`exp-3.py`)
Illustrates legitimate mutual authentication followed by an adversarial attempt to submit an intercepted response during a subsequent session with an updated challenge.

#### Execution
```bash
python exp-3.py
```

#### Output
```text
=== Challenge-Response Authentication ===
Server Challenge: 4892
Client Response: e4dfb074ca3470a24f0c978b7a4216898d254ff95b7194f41b2ffcf95a1262d1
Authentication Successful!

=== Replay Attack ===
New Server Challenge: 7130
Attacker Sends Old Response: e4dfb074ca3470a24f0c978b7a4216898d254ff95b7194f41b2ffcf95a1262d1
Replay Attack Blocked!
```

---

### B. FastAPI Microservice Prototype (`exp-3_improvement.py`)
Provides an asynchronous API service modeling server-side challenge-response generation for distributed web clients.

#### Starting the API Service
```bash
uvicorn exp-3_improvement:app --reload --port 8000
```

#### API Endpoints
- `GET /` — Health check endpoint.
- `POST /user` — Returns an ephemeral challenge nonce along with the calculated hash verification token.

#### Sample JSON Payload
```json
{
  "nonce": 38412,
  "secret": 19284,
  "hash_response": "3fa9bc8417c8ad9ef8347cf08c847a9ef3109a826471e98d89a7f309aef4190c"
}
```

---

## Defensive Engineering Insights
- **Nonce Freshness:** Because the server emits a unique, unpredictable challenge per request, previously recorded hashes cannot satisfy subsequent authorization checks.
- **Zero-Knowledge Principle:** The shared secret is never transmitted across the communication bus, preventing passive eavesdroppers on untrusted networks from acquiring credentials.
