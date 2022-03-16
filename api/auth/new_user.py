import asyncio

import aiosqlite
from encryption import encrypt_text

async def create_new_user(username : str, password : str, disabled : int = 1) -> None:
    password = await encrypt_text(password)
    async with aiosqlite.connect("api/auth/user.db") as db:
        await db.execute("""INSERT INTO Users (username, password, disabled) VALUES ("{}", "{}", {})""".format(username, password, disabled))
        await db.commit()


async def create_database() -> None:
    async with aiosqlite.connect("api/auth/user.db") as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS Users (
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            disabled INTEGER NOT NULL
            )""")
        await db.commit()


if __name__ == "__main__":
    asyncio.run(create_new_user(
        "", "", 0
    ))
    asyncio.run(create_database())