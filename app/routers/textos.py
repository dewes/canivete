from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def le_texto(texto: str):
    return texto