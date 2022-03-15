import hashlib
from dotenv import load_dotenv
import os
import binascii

def encrypt_text(text : str) -> str:
    load_dotenv()
    SALT = (os.environ["SALT"]).encode()
    ITERATIONS = int(os.environ["ITERATIONS"])

    text = text.encode()

    encrypted = hashlib.pbkdf2_hmac("sha256", text, SALT, ITERATIONS)

    return binascii.hexlify(encrypted).decode()

