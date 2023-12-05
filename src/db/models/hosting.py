from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import TimedBaseModel


class Video(TimedBaseModel):
    __tablename__ = "video"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    path: Mapped[str] = mapped_column(String(1000), unique=True)
    user_id = mapped_column(ForeignKey("user.id"))  # TODO: ondelete

    user = relationship("User", back_populates="videos")
