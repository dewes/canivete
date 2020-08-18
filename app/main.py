from typing import Optional

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel
from .routers import textos

app = FastAPI()

app.include_router(
    textos.router,
    prefix="/texto",
    tags=["texto"],
    responses={404: {
        "description": "Not found"
    }},
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
