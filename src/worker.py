import os
import time
from pathlib import Path

from dotenv import load_dotenv
from celery import Celery


_BASE_DIR = Path(__file__).resolve().parent
dotenv_path = os.path.join(_BASE_DIR, "core/.env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

celery_app = Celery(include=["src.tasks.hosting"])

celery_app.conf.broker_url = os.environ.get("REDIS_URL")
celery_app.conf.result_backend = os.environ.get("REDIS_URL")
