from typing import Annotated
from pydantic import ValidationError
from fastapi import APIRouter, Form, status, HTTPException, Depends
from sqlalchemy.orm import Session
from src.schemas.user import User, UserOut
from src.db.models.user import User as UserModel
from src.deps.db import get_db


user_router = APIRouter()


@user_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(
    username: Annotated[str, Form()], db: Annotated[Session, Depends(get_db)]
) -> UserOut:

    try:
        user = User(username=username)
    except ValidationError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Validation error")

    db_user = UserModel(**user.model_dump())
    db.add(db_user)
    db.commit()

    user_out = UserOut.model_validate(db_user)
    return user_out
