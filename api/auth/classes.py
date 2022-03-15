from dataclasses import dataclass

@dataclass
class User():
    username: str


@dataclass
class DBUser():
    username: str
    hashed_password: str
    disabled : bool
