from typing import Union

from fastapi import APIRouter, Request, Header, HTTPException
from pydantic import BaseModel

from ..auth import authenticate
from ..database import inventory_delete

tags = [{
    "name" : "Deletes from the database"
}]

delete = APIRouter()

class DeleteRequest(BaseModel):
        name : str
        amount : Union[str, int] = 1

@delete.post("/api/delete")
async def insert_into_db(request : Request, 
        delete : DeleteRequest,

        username : str = Header(None), 
        password : str = Header(None)
    ):
    
    """Updates the quantity of an item into the database, or deletes all"""

    authenticated = await authenticate(username, password)
    if authenticated != True:
        return HTTPException(403, authenticated, "JuSt gEt GoOD BRo")

    await inventory_delete(delete.name, delete.amount)
    
    if delete.amount == "all":
        return {"result" : f"All {delete.name} deleted from database"}
    return {"result" : f"Item: {delete.name} deleted from database"}