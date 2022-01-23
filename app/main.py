from fastapi import FastAPI
from api import router
from settings import get_settings

settings = get_settings()
app = FastAPI()


app.include_router(router, prefix=f"/{settings.SERVICE_NAME}")
