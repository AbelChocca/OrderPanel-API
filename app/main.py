from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import contextmanager

from app.core.settings.pydantic_setitngs import settings
from app.core.clients.cloudinary import init_cloudinary_client

@contextmanager
async def lifespan(app: FastAPI):
    init_cloudinary_client()
    yield 

app = FastAPI(
    title="Real Time Orders Panel API",
    summary="A Real time Dashboard for monitoring Orders of Any Products",
    lifespan=lifespan
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.ALLOW_ORIGINS,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)