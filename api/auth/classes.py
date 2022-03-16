from typing import Optional
# from dataclasses import dataclass

from pydantic import BaseModel

# @dataclass
# class DBUser():
#     username: str
#     hashed_password: str
#     disabled : bool

class User(BaseModel):
    username: str
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str
