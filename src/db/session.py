import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.core.settings import settings


engine = create_async_engine(settings.database_url, echo=True)
session_maker = async_sessionmaker(autoflush=False, expire_on_commit=False, bind=engine)
