from pydantic import BaseModel, ConfigDict

from src.schemas.user import User


class VideoIn(BaseModel):
    title: str
    description: str


class VideoOut(VideoIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
    path: str
    user: User
