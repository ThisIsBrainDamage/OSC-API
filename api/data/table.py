# -Standard library imports-
import os

# -Third party imports-
import asyncpg
import asyncio
from dotenv import load_dotenv

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


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.run(reset_inventory_table())