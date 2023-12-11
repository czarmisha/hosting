from sqlalchemy import insert

from src.db.models.user import User
from src.schemas import user as schemas

from .base import SQLAlchemyRepo


class UserRepo(SQLAlchemyRepo):
    async def create(self, user_in: schemas.User) -> schemas.UserOut:
        stmt = insert(User).returning(User).values(**user_in.model_dump())

        user = await self._session.scalar(stmt)

        await self._session.commit()
        return schemas.UserOut.model_validate(user)
