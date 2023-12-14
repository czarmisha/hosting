from celery import Celery

from src.core.settings import settings


celery_app = Celery(include=["src.tasks.hosting"])

celery_app.conf.broker_url = settings.redis_url
celery_app.conf.result_backend = settings.redis_url
