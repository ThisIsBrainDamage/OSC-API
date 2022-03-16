""" (module) auth_db

This contains functions related to the users db, 
This has the usernames and hashed passwords for oauth2 authentication
"""

# Standard library imports
from typing import Union, List, Tuple, Optional

# Third party imports
import aiosqlite

# Local imports-
from .encryption import encrypt_text
from .classes import UserInDB


async def create_database() -> None:
    """
    Creates the users table
    Useful when you want to reset the users
    """
    async with aiosqlite.connect("api/auth/user.db") as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS Users (
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            disabled INTEGER NOT NULL
            )""")
        await db.commit()


async def create_new_user(username : str, password : str, disabled : int = 1) -> None:
    """
    Creates a new user in the db
    This is basically a new account to be used for the oauth2 authentication

    Parameters:
        :param: username (str) : The username for the account
        :param: password (str) : The password for the account (will be stored encrypted)
        :param: disabled (int, optional) : If the account is disabled or not (0 = False, 1 = True)
    """
    password = await encrypt_text(password)
    async with aiosqlite.connect("api/auth/user.db") as db:
        await db.execute("""INSERT INTO Users (username, password, disabled) VALUES ("{}", "{}", {})""".format(username, password, disabled))
        await db.commit()


async def get_user(username : str) -> Union[bool, UserInDB]:
    """
    Gets a specific user from the Users table if not found it will return False

    Parameters:
        :param username (str) : The username to search for

    Returns:
        Union[bool, DBUser]
    """
    async with aiosqlite.connect("api/auth/user.db") as db:
        cur = await db.execute("""SELECT * FROM Users WHERE username='{}'""".format(username))
        db_result = await cur.fetchall()
        if not len(db_result):
            return False

    hashed_password = db_result[0][1]
    disabled = db_result[0][2]
        

    return UserInDB(
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
    async with aiosqlite.connect("api/auth/user.db") as db:
        data = await db.execute("SELECT * FROM Users")
        data = await data.fetchall()

    if not len(data):
        return None

    return data


# import asyncio
# if __name__ == "__main__":
#     asyncio.run(create_new_user("", "", 1))


