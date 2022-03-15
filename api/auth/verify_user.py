import os

from dotenv import load_dotenv
from pydantic import BaseModel

from utils import encrypt_text


load_dotenv()


async def authenticate(username: str, password : str):
    real_username = os.environ["USERNAME"]
    if real_username != username:
        return "Invalid Username"

    encrypted_password = encrypt_text(password)

    real_password = os.environ["PASSWORD"]
    if real_password != encrypted_password:
        return "Invalid Password"
    
    return True

class AuthDetails(BaseModel):
    username : str
    password : str
