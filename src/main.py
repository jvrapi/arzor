from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.exceptions.base import BaseError
from infra.adapters.logging import logger
from infra.config import get_settings
from presentation.api.exception_handlers import domain_exception_handler
from presentation.api.v1.routes import api_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions

    logger.info(
        "application_starting",
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

app.add_exception_handler(BaseError, domain_exception_handler)

app.include_router(api_router)


def run():
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        workers=settings.api_workers,
    )
