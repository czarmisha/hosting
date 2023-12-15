from uuid import UUID
from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str


class UserIn(User):
    password: str


class UserOut(User):
    id: UUID
