from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import TimedBaseModel
from .hosting import Video


class User(TimedBaseModel):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=sa.func.gen_random_uuid()
    )
    username: Mapped[str] = mapped_column(sa.String(50), unique=True)
    hashed_password: Mapped[str]

    videos: Mapped[list[Video]] = relationship("Video", back_populates="user")
