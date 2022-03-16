# Standard library imports
import os

# Third party imports
from fastapi import Depends, APIRouter, HTTPException
from dotenv import load_dotenv

# Local imports
from ..auth.classes import User, Item
from ..auth.authenticate import get_current_active_user
from ..data import inventory_insert, new_item


load_dotenv()

insert = APIRouter()

@insert.get("/insert_one")
async def insert_one(name : str, quantity : int = 1, current_user: User = Depends(get_current_active_user)):
    """
    Updates the quantity of an item in the db
    """
    await inventory_insert(Item(name), quantity)
    return {
            "detail" : "Item inserted into the database",
            "current_user" : current_user.username
        }


@insert.get("/new_item")
async def new_item_db(name : str, description : str, quantity : int = 1, current_user: User = Depends(get_current_active_user)):
    """
    Create new item into the database
    """
    item = Item(name, description)
    result = await new_item(item, quantity)
    if result:
        return {
            "detail" : "Item inserted into the database",
            "current_user" : current_user.username
        }
