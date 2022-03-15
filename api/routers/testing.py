import os

from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from pydantic import BaseModel

from utils import encrypt_text

load_dotenv()

tags = [
    {
        "name": "Testing"
    }
]

testing = APIRouter(tags=tags)

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

@testing.get("/auth")
async def auth(request : Request, auth_details : AuthDetails):
    authenticated = await authenticate(auth_details.username, auth_details.password)
    if authenticated != True:
        return HTTPException(403, authenticated, "JuSt gEt GoOD BRo")

    return "Nice authenticated"