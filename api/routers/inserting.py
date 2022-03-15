from fastapi import APIRouter, Request, Header, HTTPException
from pydantic import BaseModel

from ..auth import authenticate
from ..database import inventory_insert, Item

tags = [{
    "name" : "Adds to the database"
}]

insert = APIRouter()

class InsertRequest(BaseModel):
    name : str
    description : str = None
    quantity : int = 1

@insert.post("/api/insert")
async def insert_into_db(request : Request, 
        insert : InsertRequest,

        username : str = Header(None), 
        password : str = Header(None)
    ):
    
    """Updates the quantity of an item into the database, If not exists creates a new"""

    authenticated = await authenticate(username, password)
    if authenticated != True:
        return HTTPException(403, authenticated, "JuSt gEt GoOD BRo")

    item = Item(insert.name, insert.description)
    await inventory_insert(item, insert.quantity)
    return {"result" : f"Item: {insert.name} added to database"}
