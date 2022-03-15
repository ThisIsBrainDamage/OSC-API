from fastapi import APIRouter, HTTPException, Request, Header
from fastapi.responses import RedirectResponse

from ..auth import authenticate
from ..database import inventory_insert, Item, fetch_all, fetch_item

tags = [
    {
        "name": "Testing"
    }
]

testing = APIRouter(tags=tags)

@testing.get("/get_db")
async def get_db(request : Request, username : str = Header(None), password : str = Header(None)):
    authenticated = await authenticate(username, password)
    if authenticated != True:
        return HTTPException(403, authenticated, "JuSt gEt GoOD BRo")

    data = await fetch_all()

    return data