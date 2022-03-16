import hashlib
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
import binascii
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

load_dotenv()

async def encrypt_text(text : str) -> str:
    """
    Encrypts text 

    Parameters:
        text (str) : The text you want to encrypt

    Returns:
        str : The hashed text
    """
    load_dotenv()
    SALT = (os.environ["SALT"]).encode()
    ITERATIONS = int(os.environ["ITERATIONS"])

    text = text.encode()

    encrypted = hashlib.pbkdf2_hmac("sha256", text, SALT, ITERATIONS)

    return binascii.hexlify(encrypted).decode()


async def encrypt_token(key, source):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(source.encode())
    return encrypted.decode()


async def decrypt_token(key, source):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(source.encode())
    return decrypted.decode()