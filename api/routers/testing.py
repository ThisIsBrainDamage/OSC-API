from fastapi import APIRouter
from fastapi.responses import RedirectResponse

test = APIRouter()

@test.get("/test")
async def lol():
    return RedirectResponse("https://www.youtube.com/watch?v=dQw4w9WgXcQ")