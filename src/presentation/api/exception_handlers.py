from fastapi import Request
from fastapi.responses import JSONResponse

from domain.exceptions.base import BaseError


async def domain_exception_handler(request: Request, exc: BaseError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )
