"""
(module) db_functions

This module has all the database functions
These are used to insert, get or delete from the database
"""

# -Standard library imports-
import os
from typing import List, Union

# -Third party imports-
import asyncpg
import asyncio
from dotenv import load_dotenv

# -Local imports-
from classes import DataBaseItem, Item


# load enviroment variables
load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']
    

async def create_inventory_table() -> None:
    """
    Creates the Inventory table
    This will hold record of all the items
    """
    connection = await asyncpg.connect(DATABASE_URL)
    await connection.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
            ID SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(32) NOT NULL,
            description TEXT NOT NULL,
            quantity SMALLINT NOT NULL
        )""")
    await connection.close()


async def delete_inventory_table() -> None:
    """
    Deletes the inventory table
    """
    connection = await asyncpg.connect(DATABASE_URL)
    await connection.execute("""DROP TABLE IF EXISTS Inventory""")
    await connection.close()


async def reset_inventory_table() -> None:
    """
    Resets inventory table (deletes it, then creates it)
    """
    connection = await asyncpg.connect(DATABASE_URL)
    await connection.execute("""DROP TABLE IF EXISTS Inventory""")
    await connection.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
            ID SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(32) NOT NULL,
            description TEXT NOT NULL,
            quantity SMALLINT NOT NULL
        )""")
    await connection.close()


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
    print(items_list)
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
    print(item)
    return item


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
        await connection.execute("""INSERT INTO Inventory (name, description, quantity) VALUES ('{}', '{}', {})""".format(item.name, item.description, quantity))
    else:
        quantity = (item_list[0][3]) + quantity
        await connection.execute("""UPDATE Inventory SET quantity={} WHERE name='{}'""".format(quantity, item.name))
    await connection.close()


async def inventory_delete(name : str, amount : Union[int, str] = 1) -> None:
    """
    Deletes a certain amount of an item from the db or deletes the whole thing

    Parameters:
        name (str): The name of the item to delete
        amount (int or str): The amount you want to delete or if you want to delete all set this to "all"
    """
    connection = await asyncpg.connect(DATABASE_URL)
    item_list = await connection.fetch("""SELECT * FROM Inventory WHERE name='{}'""".format(name))

    if not len(item_list):
        return

    if isinstance(amount, str) and amount.lower() == "all":
        await connection.execute("""DELETE FROM Inventory WHERE name='{}'""".format(name))
    elif isinstance(amount, int):
        amount = (item_list[0][3]) - amount
        await connection.execute("""UPDATE Inventory SET quantity={} WHERE name='{}'""".format(amount, name))

    await connection.close()


# if __name__ == '__main__':
#     loop = asyncio.new_event_loop()
#     asyncio.run(reset_inventory_table())


    