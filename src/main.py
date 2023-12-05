from fastapi import FastAPI
from src.api.v1.endpoints.hosting import hosting_router
from src.api.v1.endpoints.user import user_router

app = FastAPI()

app.include_router(hosting_router, prefix='/hosting')
app.include_router(user_router, prefix='/user')


# при отправки видео создавать таск в селери и сразу отвечать что файл загружается ждите