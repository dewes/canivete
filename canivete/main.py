import os
from typing import Optional

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .routers import textos

app = FastAPI()

# Configuração para permitir execução de JS remoto
origins = [
    'http://localhost', 'https://localhost',
    os.environ.get('cors_host', '')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Apps #

# Textos #
app.include_router(
    textos.router,
    prefix="/texto",
    tags=["texto"],
    responses={404: {
        "description": "Not found"
    }},
)


# Raiz #
@app.get("/")
def read_root():
    return {"Hello": "World"}
