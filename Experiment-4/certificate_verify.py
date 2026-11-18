from cryptography import x509
from cryptography.hazmat.primitives import serialization
import hashlib


# Read Private Key

with open("private.key", "rb") as file:
    private_key = serialization.load_pem_private_key(
        file.read(),
        password=None
    )


# Read Certificate

with open("certificate.crt", "rb") as file:
    certificate_data = file.read()

certificate = x509.load_pem_x509_certificate(certificate_data)


#  Get Public Keys

public_key_from_private = private_key.public_key()
public_key_from_certificate = certificate.public_key()


# Convert Public Keys to Bytes

key1 = public_key_from_private.public_bytes(
    serialization.Encoding.DER,
    serialization.PublicFormat.SubjectPublicKeyInfo
)

key2 = public_key_from_certificate.public_bytes(
    serialization.Encoding.DER,
    serialization.PublicFormat.SubjectPublicKeyInfo
)


# Hash Both Public Keys

hash1 = hashlib.sha256(key1).hexdigest()
hash2 = hashlib.sha256(key2).hexdigest()


print("Public Key Hash from Private Key:")
print(hash1)

print("\nPublic Key Hash from Certificate:")
print(hash2)


# Compare Public Key Hashes

if hash1 == hash2:
    print("\nPublic Key: MATCH")
else:
    print("\nPublic Key: MISMATCH")
    
    
# Certificate Integrity

certificate_hash = hashlib.sha256(certificate_data).hexdigest()

print("\nCertificate SHA-256:")
print(certificate_hash)
