# Standard library imports
import os

# Third party imports
from fastapi import Depends, APIRouter, HTTPException
from dotenv import load_dotenv

# Local imports
from ..auth.classes import User
from ..auth.authenticate import get_current_active_user


load_dotenv()

users = APIRouter()

@users.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
    Get basic info on your account
    """
    return current_user