"""
This is the main file for the api
Contains config for the api and other info
"""


__author__ = "Siddhesh Zantye"
__version__ = 0.1


# -Standard library imports-

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
import uvicorn

# -Local imports- 
from api import oauth, users


limiter = Limiter(key_func=get_remote_address)

# Description for api docs
description = """
### API for osc inventory website
"""

# Creates an instance of the FastAPI class
app = FastAPI(
    title = "OSC-API",
    description=description,
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Adding rate limiting for the api
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Added CORS, Probably will delete this because it isnt being used at the moment
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


# Routers
app.include_router(oauth)
app.include_router(users)


# Other
@app.get("/")
async def home(request : Request):
    """
    Home Page - Redirects to docs
    """
    return RedirectResponse("/docs")


# Run
if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)