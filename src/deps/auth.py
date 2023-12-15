from fastapi import Depends

from src.deps.repo import get_repo
from src.repos.user import UserRepo
from src.services.auth import Authenticator


async def get_user(
    token: str = Depends(Authenticator.auth_scheme),
    authenticator: Authenticator = Depends(),
    user_repo: UserRepo = Depends(get_repo(UserRepo)),
):
    user_in = authenticator.validated_token_payload(token)
    user = await user_repo.get_by_username(user_in.username)
    return user
