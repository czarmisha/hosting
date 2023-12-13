import shutil
import aiofiles

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    Header,
    HTTPException,
    Request,
    UploadFile,
    status,
)
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from celery.result import AsyncResult

from src.deps.repo import get_repo
from src.tasks.hosting import test_task
from src.repos.hosting import VideoRepo
from src.schemas import hosting as schemas
from src.services.hosting import read_video_range

hosting_router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@hosting_router.post("/upload", status_code=status.HTTP_201_CREATED)
async def root(
    user_id: int = Form(),
    title: str = Form(),
    description: str = Form(),
    file: UploadFile = File(),
    repo: VideoRepo = Depends(get_repo(VideoRepo)),
) -> schemas.VideoOut:
    try:
        video_in = schemas.VideoIn(title=title, description=description)
    except ValidationError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Validation error")

    async with aiofiles.open(f"media/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    task = test_task.delay(5)
    print("create task with id:", task)

    video = await repo.create(video_in, path=f"media/{file.filename}", user_id=user_id)
    return video


@hosting_router.get("/{video_id}")
async def get_streaming_vide(
    video_id: int, range: str = Header(), repo: VideoRepo = Depends(get_repo(VideoRepo))
):
    video = await repo.get_by_id(video_id)
    return await read_video_range(range, video.path)


@hosting_router.get("/")
async def read_root(request: Request, repo: VideoRepo = Depends(get_repo(VideoRepo))):
    videos = await repo.get_videos()
    return templates.TemplateResponse(
        "index.html", context={"request": request, "videos": videos}
    )


@hosting_router.get("/status/{task_id}")
async def get_video_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
