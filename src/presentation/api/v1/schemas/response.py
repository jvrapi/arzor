from pydantic import BaseModel


class ErrorResponse(BaseModel):
    detail: str


NotFoundResponse = {
    "model": ErrorResponse,
    "description": "Resource not found",
}

BadRequestResponse = {
    "model": ErrorResponse,
    "description": "Bad request",
}
