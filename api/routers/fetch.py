# Standard library imports
import os

# Third party imports
from fastapi import Depends, APIRouter, HTTPException
from dotenv import load_dotenv

# Local imports
from ..auth.classes import User
from ..auth.authenticate import get_current_active_user
from ..data import fetch_all, fetch_item


load_dotenv()

fetch = APIRouter()

@fetch.get("/find")
async def get_by_name(name : str, current_user: User = Depends(get_current_active_user)):
    """
    Looks for an item in the database
    """
    data = await fetch_item(name)
    if data is None:
        return HTTPException(404, "Item not found")
    return data


@fetch.get("/get_all")
async def get_all(current_user: User = Depends(get_current_active_user)):
    """
    Gets all items from the database
    """
    data = await fetch_all()

    return data