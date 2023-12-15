from sqlalchemy import insert, select

from src.db.models.user import User
from src.schemas import user as schemas

from .base import SQLAlchemyRepo


class UserRepo(SQLAlchemyRepo):
    async def create(
        self, user_in: schemas.UserIn, hashed_password: str
    ) -> schemas.UserOut:
        stmt = (
            insert(User)
            .returning(User)
            .values(username=user_in.username, hashed_password=hashed_password)
        )

        user = await self._session.scalar(stmt)

        await self._session.commit()
        return schemas.UserOut.model_validate(user)

    async def get_by_username(self, username: str) -> User:
        stmt = select(User).where(User.username == username)

        result = await self._session.scalar(stmt)

        if result is None:
            return

        return result
