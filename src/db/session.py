from pathlib import Path
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv


_BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(_BASE_DIR, 'core/.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

engine = create_engine(os.environ.get("DATABASE_URL"))


def create_session():
    with Session(engine) as session:
        return session