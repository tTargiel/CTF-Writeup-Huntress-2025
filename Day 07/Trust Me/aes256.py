import base64
from Crypto.Cipher import AES

# Input parameters
aes_key_b64 = "xck724QVNPrlVF7csPEgQdEM1NkO4Wp9gjX6ZXyTgl0="
iv_hex = "04c9e65365568d0f8a02f526ba00fc5b"
ciphertext_b64 = "Wx6eETGXddnmCT4qZ7BxgRYpC+kdjjFzXxW+BM4HiI3GPaslpFBnpk9XplnaSxNg"

# Conversion of key and IV
key = base64.b64decode(aes_key_b64)
iv = bytes.fromhex(iv_hex)
ciphertext = base64.b64decode(ciphertext_b64)

# Decryption AES-256-CBC
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

# Removal of PKCS#7 padding (if present)
def remove_pkcs7_padding(data):
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 16:
        return data  # invalid padding
    return data[:-pad_len]

plaintext = remove_pkcs7_padding(plaintext)

print(plaintext.decode('utf-8', errors='replace'))
