import os

from dotenv import load_dotenv
import asyncpg
import asyncio

load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


async def create_database():
    connection = await asyncpg.connect(DATABASE_URL)
    await connection.execute("""CREATE TABLE Inventory (
            ID SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(32) NOT NULL,
            description TEXT NOT NULL,
            quantity SMALLINT NOT NULL
        )""")
    await connection.close()


async def insert():
    connection = await asyncpg.connect(DATABASE_URL)
    await connection.execute("""INSERT INTO Inventory (name, description, quantity) VALUES ('test1', 'A very nice test lol', 1)""")
    await connection.close()


async def select():
    connection = await asyncpg.connect(DATABASE_URL)
    cur = await connection.fetch("""SELECT * FROM Inventory""")
    print(cur)
    await connection.close()


# class Item():
#     def __init__(self, 
#             name : str,
#         ) -> None:
#         pass

loop = asyncio.new_event_loop()
asyncio.run(select())