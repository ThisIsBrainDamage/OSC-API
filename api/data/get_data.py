# -Standard library imports-
import os
from typing import List, Union

# -Third party imports-
import asyncpg
from dotenv import load_dotenv

# -Local imports-
from ..auth.classes import DataBaseItem


# load enviroment variables
load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


async def fetch_all() -> Union[List[asyncpg.Record], None]:
    """
    Fetches ALL items/record from the inventory table
    Returns:
        List[asyncpg.Record] or None
    """
    connection = await asyncpg.connect(DATABASE_URL)
    items_list = await connection.fetch("""SELECT * FROM Inventory""")
    await connection.close()

    if not len(items_list):
        return None

    return items_list


async def fetch_item(name : str) -> Union[DataBaseItem, None]:
    """
    Fetches a specific item from the inventory table
    Parameters:
        name (str) : The name of the item
    Returns:
        DataBaseItem or None
    """
    connection = await asyncpg.connect(DATABASE_URL)
    item_list = await connection.fetch("""SELECT * FROM Inventory Where name='{}'""".format(name))
    await connection.close()

    if not len(item_list):
        return None
    
    item = item_list[0]

    item = DataBaseItem(
        item[0],
        item[1],
        item[2],
        item[3]
    )
    
    return item