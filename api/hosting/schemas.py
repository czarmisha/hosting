from pydantic import BaseModel

from api.user.schemas import User


class VideoInfo(BaseModel):
    title: str
    description: str


class UploadVideoInfo(VideoInfo):
    pass


class DBVideoInfo(VideoInfo):
    id: int
    

class UserVideoInfo(BaseModel):
    user: User
    video_info: DBVideoInfo
