from fastapi import APIRouter, Depends, HTTPException, status

from src.schemas import user as user_schemas, auth as auth_schemas
from src.deps.repo import get_repo
from src.repos.user import UserRepo
from src.services.auth import Authenticator

auth_router = APIRouter()


@auth_router.post("/access-token")
async def get_access_token(
    user_in: user_schemas.UserIn,
    authenticator: Authenticator = Depends(),
    user_repo: UserRepo = Depends(get_repo(UserRepo)),
) -> auth_schemas.Token:
    """
    Retrieve access-token
    """
    user = await authenticator.authenticate_user(
        user_repo=user_repo, username=user_in.username, password=user_in.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = authenticator.create_access_token(user)

    return auth_schemas.Token(access_token=access_token)
