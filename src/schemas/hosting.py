from pydantic import BaseModel, ConfigDict

from src.schemas.user import User


class VideoIn(BaseModel):
    title: str
    description: str


class VideoOut(VideoIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    path: str
    user: User


class VideosOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    videos: list[VideoOut]
