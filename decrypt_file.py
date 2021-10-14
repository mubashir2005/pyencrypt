import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


fkey = input("Enter your key").encode()
mysalt = b'\xe2\x12\xf0\xdb\xfe\xed\xa7{\xcb\xfe\x1e-\xac\xc2p\x91'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=mysalt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(fkey)).decode()
cipher = Fernet(key)

with open("secret-wallet.pdf_encrypted", 'rb') as df:
    encrypted_data = df.read()

decrypted_file = cipher.decrypt(encrypted_data)

with open("secretwallet.pdf", 'wb') as df:
    df.write(decrypted_file)
