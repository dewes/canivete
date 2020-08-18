import re
from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional, List

router = APIRouter()


class Texto(BaseModel):
    """ Classe para definir o modelo a ser passado via JSON para as funções. """
    texto: str

    class Config:
        schema_extra = {
            "example": {
                "texto":
                "Um texto contendo dados como Nomes, Emails, Telefones."
            }
        }


@router.get("/")
def le_texto(texto: str):
    return texto


@router.post("/nomes")
def extrai_nomes(texto: Texto):
    return None


@router.post("/emails", response_model=List[str])
def extrai_emails(texto: Texto):
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
