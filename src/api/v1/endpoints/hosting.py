import shutil
from fastapi import APIRouter, UploadFile, Form, Request
from typing import Annotated
from src.schemas.hosting import UploadVideoInfo

hosting_router = APIRouter()


@hosting_router.post('/upload')
async def root(
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    file: UploadFile
):
    video_info = UploadVideoInfo(title=title, description=description)
    # with open(file.filename, 'wb') as buffer:
    #     shutil.copyfileobj(file.file, buffer)
    return {'filename': file.filename, 'info': video_info}
