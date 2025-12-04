from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infra.config import get_settings
from infra.logging import logger

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions

    logger.info(
        "application_starting",
        service_name=settings.service_name,
        environment=settings.environment,
    )
    logger.info("application_ready")
    yield
    # Shutdown actions
    logger.info("application_shutting_down")


app = FastAPI(
    title="API Boilerplate",
    description="API Bolilerplate with FastAPI, Pydantic, and Uvicorn",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def run():
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        workers=settings.API_WORKERS,
    )
