# Experiment 8: Send and Receive PGP Encrypted Email Using Thunderbird

## Aim

To send and receive PGP-encrypted emails using Thunderbird and understand secure email communication through encryption and digital signatures.

---

## Objective

The objectives of this experiment are:

- To configure an email account in Mozilla Thunderbird.
- To enable the Primary Password feature to protect stored credentials and secret keys.
- To generate an OpenPGP public and private key pair.
- To examine the key fingerprint and expiry date.
- To securely back up the personal secret key.
- To exchange public keys between the sender and recipient.
- To verify the authenticity of an exchanged public key using its fingerprint.
- To send and receive encrypted emails using OpenPGP.
- To verify digital signatures and decrypt received messages.
- To demonstrate secure file sharing through encrypted email attachments.

---

## Requirements

- Mozilla Thunderbird
- An active email account
- OpenPGP support in Thunderbird
- A communication partner with an OpenPGP key pair
- Internet connection
- GitHub
- Basic knowledge of public-key cryptography and digital signatures

---

## Theory

### PGP (Pretty Good Privacy)

PGP is a cryptographic method used to secure emails and files through encryption and digital signatures. It provides confidentiality, authentication, and integrity during communication.

### OpenPGP

OpenPGP is an open standard for implementing PGP-based encryption and digital signatures. It is supported by applications such as Mozilla Thunderbird.

### Public Key and Private Key

A public key can be shared with other users and is used to encrypt messages or verify digital signatures.

A private key is kept secret by its owner and is used to decrypt received messages or create digital signatures.

### Encryption and Decryption

Encryption converts readable data into ciphertext using the recipient's public key. Decryption converts the ciphertext back into readable form using the recipient's corresponding private key.

### Digital Signature

A digital signature is created using the sender's private key. It helps verify the sender's authenticity and ensures that the message has not been modified after signing.

### Key Fingerprint

A key fingerprint is a unique value associated with an OpenPGP key. It is used to verify the authenticity of a public key through a trusted communication channel.

---

## Procedure

### Step 1: Configure the Email Account

Mozilla Thunderbird was opened, and the assigned lab email account was configured.

The Inbox was accessed to verify that the email account was successfully configured and ready for communication.

![Step 1: Thunderbird email account configuration](Outputs/ss1.png)

---

### Step 2: Enable Primary Password

The Primary Password feature was enabled in Thunderbird's settings.

This feature helps protect stored account credentials and secret keys by requiring the primary password when accessing protected information.

The configuration was checked without exposing the actual password.

![Step 2: Primary Password configuration](Outputs/ss2.png)

---

### Step 3: Generate an OpenPGP Key Pair

An OpenPGP key pair was generated for the configured email identity.

The generated key pair consisted of:

- **Public Key:** Shared with other users for encryption and signature verification.
- **Private Key:** Kept securely by its owner for decryption and digital signing.

The generated key's User ID, fingerprint, and expiry date were examined and recorded.

![Step 3: OpenPGP key generation and details](Outputs/ss3.png)

---

### Step 4: Manage and Back Up the Secret Key

The OpenPGP Key Manager was opened to inspect the generated personal key.

The secret key was exported and securely backed up to preserve access to encrypted communications.

The backup operation was confirmed through Thunderbird's key-management interface.

The secret key backup was kept secure and was not included in the public GitHub repository.

![Step 4: OpenPGP Key Manager and secret-key backup](Outputs/ss4.png)

---

### Step 5: Exchange Public Keys

The personal public key was attached to a key-introduction email and shared with the communication partner.

The partner's public key was also received and imported into Thunderbird.

This exchange allowed both users to obtain the public keys required for encrypted communication and digital-signature verification.

![Step 5: Public-key exchange](Outputs/ss5.png)

---

### Step 6: Verify the Partner's Public Key

The partner's OpenPGP key fingerprint was compared through a separate trusted communication channel.

After confirming that the fingerprints matched, the partner's public key was accepted for encryption and signature verification.

Fingerprint verification helped establish trust in the exchanged public key and reduced the risk of using an impersonated key.

![Step 6: Public-key fingerprint verification](Outputs/ss6.png)

---

### Step 7: Compose and Send an Encrypted Email

A new email was composed in Thunderbird and addressed to the communication partner.

Before sending the message, both security options were enabled:

- **OpenPGP Encryption:** Ensures that only the intended recipient can decrypt and read the message.
- **Digital Signature:** Allows the recipient to verify the sender's authenticity and message integrity.

The email was sent with both encryption and digital signature enabled.

![Step 7: Encrypted and digitally signed email](Outputs/ss7.png)

---

### Step 8: Receive, Decrypt, and Verify the Email

The recipient opened the received email in Thunderbird.

The encrypted message was successfully decrypted using the recipient's private key.

The message security details were inspected to verify the encryption and digital signature status.

Thunderbird displayed the following security indicators:

- **Good Digital Signature**
- **Message Is Encrypted**

These indicators demonstrated that the message was successfully decrypted and its digital signature was verified.

![Step 8: Received email, decryption and signature verification](Outputs/ss8.png)

---

## Improvement: Encrypted and Digitally Signed File Attachment

### Description

As an improvement to the basic experiment, secure file sharing was demonstrated by creating a confidential text file named `confidential.txt` and attaching it to a new email.

OpenPGP encryption and digital signature options were enabled before sending the email to the communication partner.

The recipient decrypted the received email and accessed the protected attachment.

This extended the experiment beyond secure email communication and demonstrated how OpenPGP can also protect file sharing through encrypted and digitally signed email attachments.

---

## Files Included

### Public-Key Files

The `Outputs` folder contains the following exported public keys:

- [`Tanish Sharma publickey.asc`](Outputs/Tanish%20Sharma%20publickey.asc) — Public key generated for the sender's email identity.
- [`Abhishek Sharma publickey.asc`](Outputs/Abhishek%20Sharma%20publickey.asc) — Communication partner's public key exchanged and imported during the experiment.

These files can be imported into compatible OpenPGP applications for public-key encryption and digital-signature verification.

### Output Files

The `Outputs` folder contains the following screenshots:

- `ss1.png` — Thunderbird email account configuration.
- `ss2.png` — Primary Password configuration.
- `ss3.png` — OpenPGP key generation and details.
- `ss4.png` — OpenPGP Key Manager and secret-key backup.
- `ss5.png` — Public-key exchange.
- `ss6.png` — Fingerprint verification and public-key acceptance.
- `ss7.png` — Encrypted and digitally signed email.
- `ss8.png` — Received email, decryption, and signature verification.

---

## Result

An OpenPGP key pair was generated and managed using Mozilla Thunderbird. Public keys were exchanged between the sender and recipient, and the partner's key fingerprint was verified before use.

An email was successfully sent using encryption and digital signature, and the received message was decrypted and its signature verified.

As an improvement, an encrypted and digitally signed email attachment was also used to demonstrate secure file sharing.

---

## Conclusion

The experiment demonstrated secure email communication using OpenPGP in Mozilla Thunderbird. Public-key encryption provided confidentiality, private-key decryption allowed the recipient to access the original message, and digital signatures helped verify authenticity and integrity.

The additional attachment-encryption activity further demonstrated how OpenPGP security mechanisms can be used to protect both email messages and file sharing.
