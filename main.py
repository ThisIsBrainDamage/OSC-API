"""
This is the main file for the api
Contains config for the api and other info
"""

__author__ = "Siddhesh Zantye"
__version__ = 0.1

# -Standard library imports-
import os

# -Third party imports-
# Fastapi
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

# Slowapi for rate limits
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Other imports
from dotenv import load_dotenv
import uvicorn

# -Local imports-
from api.routers import test

# --End of imports--

limiter = Limiter(key_func=get_remote_address)

# Description for api docs
description = """
### API TestOSCAPI
"""

# Creates an instance of the FastAPI class
app = FastAPI(
    title = "TestOSCAPI",
    description=description,
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]

# Endpoitns

app.include_router(test)

@app.get("/")
async def home(request : Request):
    """
    Home Page - Redirects to docs
    """
    return RedirectResponse("/docs")

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)