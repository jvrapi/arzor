from .base import BaseError


class EntityAlreadyExistsError(BaseError):
    """
    Raised when attempting to create an entity that already exists.
    """

    status_code = 409
    default_message = "Entity already exists"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)
