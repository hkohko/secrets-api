from fastapi import APIRouter
from app.generate_password import token

router = APIRouter()

@router.get("/token/{length}")
async def send_result(length: int):
    return token.generate_token(entry=length)
