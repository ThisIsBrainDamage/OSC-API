# Standard library imports
import os

# Third party imports
from fastapi import Depends, APIRouter, HTTPException
from dotenv import load_dotenv

# Local imports
from ..auth.classes import User
from ..auth.authenticate import get_current_active_user
from ..data import inventory_delete


load_dotenv()

delete = APIRouter()

@delete.get("/delete_one")
async def delete_one(name : str, quantity : int = 1, current_user: User = Depends(get_current_active_user)):
    """
    Updates the quantity of an item (lowers it) in the database
    """
    await inventory_delete(name, quantity)
    return {
        "detail" : f"Deleted {quantity} {name} from db",
        "current_user" : current_user.username
    }


@delete.get("/delete_all")
async def delete_all(name : str, current_user: User = Depends(get_current_active_user)):
    """
    Deletes all of an item from the database
    """
    await inventory_delete(name, "all")
    return {
        "detail" : f"Deleted all of {name} from db",
        "current_user" : current_user.username
    }
    