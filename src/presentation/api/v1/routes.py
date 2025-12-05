from fastapi import APIRouter

from .controllers import set_controller

api_router = APIRouter()

api_router.include_router(set_controller.router, prefix="/api/v1")
