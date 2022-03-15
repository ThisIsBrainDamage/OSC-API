"""
(module) classes

Some dataclasses for making the database items more simple
"""

from dataclasses import dataclass

@dataclass
class Item():
    """
    This class is used to create a new item or insert one
    """
    name : str
    description : str = None

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