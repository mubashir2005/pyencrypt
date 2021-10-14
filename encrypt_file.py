import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from cryptography.fernet import Fernet

user_password = input("Enter password")
password = user_password.encode()

mysalt = b'\xe2\x12\xf0\xdb\xfe\xed\xa7{\xcb\xfe\x1e-\xac\xc2p\x91'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=mysalt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password)).decode()
cipher = Fernet(key)

file = "Busy people’s guide to sleep.pdf"
with open(file, 'rb') as f:
    data = f.read()

encrypted_file = cipher.encrypt(data)

with open(file + "_encrypted", 'wb') as f:
    f.write(encrypted_file)
