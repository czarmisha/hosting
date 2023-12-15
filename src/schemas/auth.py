from uuid import UUID

from pydantic import BaseModel

from src.schemas import user as user_schemas


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class TokenSub(BaseModel):
    user_id: UUID


class TokenPayload(BaseModel):
    sub: TokenSub
    exp: int
