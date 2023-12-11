from sqlalchemy import insert, select
from sqlalchemy.orm import joinedload

from src.db.models.hosting import Video
from src.schemas import hosting as schemas

from .base import SQLAlchemyRepo


class VideoRepo(SQLAlchemyRepo):
    async def create(
        self, video_in: schemas.VideoIn, path: str, user_id: int
    ) -> schemas.VideoOut:
        stmt = (
            insert(Video)
            .returning(Video)
            .values(
                path=path,
                user_id=user_id,
                **video_in.model_dump(),
            )
        ).options(joinedload(Video.user))

        video = await self._session.scalar(stmt)

        await self._session.commit()
        await self._session.refresh(video)
        return schemas.VideoOut.model_validate(video)

    async def get_by_id(self, id: int) -> schemas.VideoOut:
        stmt = select(Video).where(Video.id == id).options(joinedload(Video.user))
        video = await self._session.scalar(stmt)
        await self._session.refresh(video)

        return schemas.VideoOut.model_validate(video)
