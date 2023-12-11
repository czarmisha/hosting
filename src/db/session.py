import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

_BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(_BASE_DIR, "core/.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

engine = create_async_engine(os.environ.get("DATABASE_URL"), echo=True)
session_maker = async_sessionmaker(autoflush=False, expire_on_commit=False, bind=engine)
