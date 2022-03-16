# -Standard library imports-
import os
from typing import Union

# -Third party imports-
import asyncpg
from dotenv import load_dotenv

# load enviroment variables
load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


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

    try:
        amount = int(amount)
        amount = (item_list[0][3]) - amount
        await connection.execute("""UPDATE Inventory SET quantity={} WHERE name='{}'""".format(amount, name))
    except ValueError:
        if amount.lower() == "all":
            await connection.execute("""DELETE FROM Inventory WHERE name='{}'""".format(name))
            
    await connection.close()