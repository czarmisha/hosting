import shutil
from fastapi import APIRouter, UploadFile, Form, Request
from typing import Annotated
from api.hosting.schemas import UploadVideoInfo

hosting_app = APIRouter()


@hosting_app.post('/upload')
async def root(
    req: Request,
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    file: UploadFile
):
    video_info = UploadVideoInfo(title=title, description=description)
    # with open(file.filename, 'wb') as buffer:
    #     shutil.copyfileobj(file.file, buffer)
    return {'filename': file.filename, 'info': video_info}
