from typing import Optional
from dataclasses import dataclass

from pydantic import BaseModel

class User(BaseModel):
    """
    A base User - Used for authentication so its easier
    """
    username: str
    disabled: Optional[bool] = None
    

class UserInDB(User):
    """
    A subclass of `User` with the `hashed_password` attribute
    """
    hashed_password: str


@dataclass
class DataBaseItem():
    """
    This is a database item.
    It usually takes in and asyncpg.Record class and makes it into a dataclass
    This is for simplicity because asyncpg.Record is a list and this is a class
    """
    record_id : int
    name : str
    description : str
    quantity : int


@dataclass
class Item():
    """
    This class is used to create a new item or insert one
    """
    name : str
    description : str = None