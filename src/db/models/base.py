import datetime

from sqlalchemy import sql
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseDBModel(DeclarativeBase):
    pass


class TimedBaseModel(BaseDBModel):
    """
    An abstract base model that adds created_at and updated_at timestamp fields to the model
    """

    __abstract__ = True

    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=sql.func.now()
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False,
        server_default=sql.func.now(),
        onupdate=sql.func.now(),
    )
