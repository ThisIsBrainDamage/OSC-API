from typing import Union, List, Tuple, Optional

import aiosqlite
import hashlib
from dotenv import load_dotenv
import os
import binascii

from classes import DBUser

async def encrypt_text(text : str) -> str:
    """
    Encrypts text 

    Parameters:
        text (str) : The text you want to encrypt

    Returns:
        str : The hashed text
    """
    load_dotenv()
    SALT = (os.environ["SALT"]).encode()
    ITERATIONS = int(os.environ["ITERATIONS"])

    text = text.encode()

    encrypted = hashlib.pbkdf2_hmac("sha256", text, SALT, ITERATIONS)

    return binascii.hexlify(encrypted).decode()

async def create_database() -> None:
    """
    Creates the users table
    Useful when you want to reset the users
    """
    async with aiosqlite.connect("user.db") as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS Users (
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            disabled INTEGER NOT NULL
            )""")
        await db.commit()


async def create_new_user(username : str, password : str, disabled : int = 1) -> None:
    password = await encrypt_text(password)
    async with aiosqlite.connect("user.db") as db:
        await db.execute("""INSERT INTO Users (username, password, disabled) VALUES ("{}", "{}", {})""".format(username, password, disabled))
        await db.commit()


async def get_user(username : str) -> Union[bool, DBUser]:
    """
    Gets a specific user from the Users table if not found it will return False

    Parameters:
        username (str) : The username to search for

    Returns:
        Union[bool, DBUser]
    """
    async with aiosqlite.connect("user.db") as db:
        cur = await db.execute("""SELECT * FROM Users WHERE username='{}'""".format(username))
        db_result = await cur.fetchall()
        if not len(db_result):
            return False

    hashed_password = db_result[0][1]
    disabled = db_result[0][2]
        

    return DBUser(
        username=username,  
        hashed_password=hashed_password, 
        disabled=disabled
    )


async def get_all_users() -> Optional[List[Tuple]]:
    """
    Fetches all users from the database (Users table)

    Returns:
        Optional[List[Tuple]]
    """
    async with aiosqlite.connect("user.db") as db:
        data = await db.execute("SELECT * FROM Users")
        data = await data.fetchall()

    if not len(data):
        return None

    return data