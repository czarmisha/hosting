from fastapi import APIRouter, Depends, Form, HTTPException, status
from pydantic import ValidationError

from src.deps.repo import get_repo
from src.repos.user import UserRepo
from src.schemas.user import UserIn, UserOut
from src.services.auth import Authenticator

user_router = APIRouter()


@user_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    username: str = Form(),
    password: str = Form(),
    auth_service: Authenticator = Depends(),
    user_repo: UserRepo = Depends(get_repo(UserRepo)),
) -> UserOut:

    try:
        user = UserIn(username=username, password=password)
    except ValidationError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Validation error")

    hashed_password = auth_service.get_password_hash(user.password)
    user = await user_repo.create(user, hashed_password)
    return user


# TODO: get user by username
