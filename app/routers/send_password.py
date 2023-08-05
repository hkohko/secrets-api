from fastapi import APIRouter
from internals import token

router = APIRouter()


@router.get("/token/{length}")
async def send_result(length: int):
    return token.generate_token(entry=length)
