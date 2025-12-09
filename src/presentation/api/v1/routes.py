from fastapi import APIRouter

from .controllers import card_router, set_router

api_router = APIRouter()

api_router.include_router(set_router, prefix="/api/v1")
api_router.include_router(card_router, prefix="/api/v1")
