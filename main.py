from fastapi import FastAPI
from api.hosting.routes import hosting_app

app = FastAPI()

app.include_router(hosting_app, prefix='/hosting')


# при отправки видео создавать таск в селери и сразу отвечать что файл загружается ждите