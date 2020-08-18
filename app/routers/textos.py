import re
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()


class Texto(BaseModel):
    texto: str

    class Config:
        schema_extra = {
            "example": {
                "texto":
                "Um texto bem comprido contendo dados como Nomes, Emails, Telefones."
            }
        }


@router.get("/")
def le_texto(texto: str):
    return texto


@router.post("/nomes")
def extrai_nomes(texto: Texto):
    return None


@router.post("/emails")
def extrai_emails(texto: Texto) -> list:
    """ Procura emails mencionados no documento. """
    exp = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    emails = exp.findall(texto.texto)
    return emails


@router.post('/telefones')
def extrai_telefones(texto: Texto):
    """ Procura telefones mencionados no documento. """
    exp = re.compile(r"\(?\d{2}\)?\s?\d{4,5}\-?\d{4}")
    telefones = exp.findall(texto.texto)
    return telefones
