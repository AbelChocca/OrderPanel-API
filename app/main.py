from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.settings.pydantic_setitngs import settings
from app.core.clients.cloudinary import init_cloudinary_client

from app.infra.messaging.kafka.clients.producer import kafka_producer

from app.api.graphql.router import graphql_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_cloudinary_client()
    await kafka_producer.start()
    yield 

    await kafka_producer.stop()

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

app.include_router(graphql_router, prefix="/graphql")