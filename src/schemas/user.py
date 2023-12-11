from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str


class UserOut(User):
    model_config = ConfigDict(from_attributes=True)

    id: int
