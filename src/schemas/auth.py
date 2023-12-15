from pydantic import BaseModel

from src.schemas import user as user_schemas


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class TokenPayload(BaseModel):
    user: user_schemas.UserOut
