from fastapi import (APIRouter, Depends, File, Form, HTTPException, UploadFile,
                     status)
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from starlette.requests import Request

from src.deps.repo import get_repo
from src.repos.hosting import VideoRepo
from src.schemas import hosting as schemas

hosting_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@hosting_router.post("/upload", status_code=status.HTTP_201_CREATED)
async def root(
    user_id: int = Form(),
    title: str = Form(),
    description: str = Form(),
    file: UploadFile = File(),
    video_repo: VideoRepo = Depends(get_repo(VideoRepo)),
) -> schemas.VideoOut:
    try:
        video_in = schemas.VideoIn(title=title, description=description)
    except ValidationError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Validation error")

    # with open(file.filename, 'wb') as buffer:
    #     shutil.copyfileobj(file.file, buffer)

    video = await video_repo.create(video_in, path=file.filename, user_id=user_id)
    return video


@hosting_router.get("/{video_id}")
async def get_streaming_vide(request: Request, video_id: int):
    pass
