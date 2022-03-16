# -Standard library imports-
import os
from typing import List, Union

# -Third party imports-
import asyncpg
from dotenv import load_dotenv

# -Local imports-
from ..auth.classes import Item

# load enviroment variables
load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


async def inventory_insert(item : Item, quantity : int = 1) -> None:
    """
    Updates the quantity of an item in the database or creates a new item
    Parameters:
        item (Item): The item to add to / create
        quantity (int): The amount you want to add
    """
    connection = await asyncpg.connect(DATABASE_URL)
    item_list = await connection.fetch("""SELECT * FROM Inventory WHERE name='{}'""".format(item.name))
    if not len(item_list):
        await connection.close()
        return "Item doesn't exist"
    else:
        quantity = (item_list[0][3]) + quantity
        await connection.execute("""UPDATE Inventory SET quantity={} WHERE name='{}'""".format(quantity, item.name))
    await connection.close()


async def new_item(item : Item, quantity : int = 1) -> None:
    """
    Updates the quantity of an item in the database or creates a new item
    Parameters:
        item (Item): The item to add to / create
        quantity (int): The amount you want to add
    """
    connection = await asyncpg.connect(DATABASE_URL)
    item_list = await connection.fetch("""SELECT * FROM Inventory WHERE name='{}'""".format(item.name))
    if not len(item_list):
        await connection.execute("""INSERT INTO Inventory (name, description, quantity) VALUES ('{}', '{}', {})""".format(item.name, item.description, quantity))
    else:
        await connection.close()
        return "Item already exists"
    await connection.close()
