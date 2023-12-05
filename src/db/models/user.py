from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import TimedBaseModel
from .hosting import Video


class User(TimedBaseModel):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)

    videos: Mapped[list[Video]] = relationship(back_populates='user')
