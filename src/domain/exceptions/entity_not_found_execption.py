from .base import BaseError


class EntityNotFoundError(BaseError):
    """
    Raised when an entity is not found in a repository.
    """

    status_code = 404
    default_message = "Entity not found"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)
