from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, status
from pydantic import ValidationError
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.user import User as UserModel
from src.deps.session import get_session
from src.schemas.user import User, UserOut

user_router = APIRouter()


@user_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    username: Annotated[str, Form()],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> UserOut:

    try:
        user = User(username=username)
    except ValidationError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Validation error")

    stmt = insert(UserModel).returning(UserModel).values(**user.model_dump())
    db_user = await session.scalar(stmt)
    await session.commit()
    user_out = UserOut.model_validate(db_user)
    return user_out
