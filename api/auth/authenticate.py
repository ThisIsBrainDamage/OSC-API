from typing import Optional

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dotenv import load_dotenv

from users_db_functions import get_all_users, get_user, create_database, create_new_user, encrypt_text
from classes import User, DBUser

load_dotenv()


testing = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@testing.post("/token")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):

    # raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    token = await encrypt_text(f"{form_data.username}{form_data.password}")
    return {"access_token": token, "token_type": "bearer"}


@testing.get()
async def test_endpoint(user: User = Depends()):
    return "Success!"