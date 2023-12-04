from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from db.base import BaseDBModel
from api.user.models import User


class Video(BaseDBModel):
    __tablename__ = 'video'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    path: Mapped[str] = mapped_column(String(1000), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())
    user_id = mapped_column(ForeignKey('user.id'))
    
    user: Mapped[User] = relationship(back_populates='videos')
