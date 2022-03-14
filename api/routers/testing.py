from fastapi import APIRouter
from fastapi.responses import RedirectResponse

test = APIRouter()

@test.get("/test")
async def lol():
    from main import DATABASE_URL
    print(DATABASE_URL)
    return RedirectResponse("https://www.youtube.com/watch?v=dQw4w9WgXcQ")