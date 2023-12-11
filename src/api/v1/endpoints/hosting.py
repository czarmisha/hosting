import shutil

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    Header,
    HTTPException,
    Request,
    Response,
    UploadFile,
    status,
)
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from src.deps.repo import get_repo
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

    with open(f"media/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    video = await repo.create(video_in, path=f"media/{file.filename}", user_id=user_id)
    return video


@hosting_router.get("/{video_id}")
async def get_streaming_vide(
    video_id: int, range: str = Header(), repo: VideoRepo = Depends(get_repo(VideoRepo))
):
    video = await repo.get_by_id(video_id)
    return await read_video_range(range, video.path)


@hosting_router.get("/")
async def read_root(request: Request):
    # TODO: return for example last 5 videos(id, title and description)
    return templates.TemplateResponse("index.html", context={"request": request})
