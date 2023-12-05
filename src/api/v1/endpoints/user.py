from fastapi import APIRouter, Depends, Form, HTTPException, status
from pydantic import ValidationError

from src.deps.repo import get_repo
from src.repos.user import UserRepo
from src.schemas.user import User, UserOut

user_router = APIRouter()


@user_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    username: str = Form(),
    user_repo: UserRepo = Depends(get_repo(UserRepo)),
) -> UserOut:

    try:
        user = User(username=username)
    except ValidationError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Validation error")

    user = await user_repo.create(user)
    return user
