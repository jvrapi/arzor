from .base import BaseError


class ValidationError(BaseError):
    """
    Raised when fields are not valid.
    """

    status_code = 400
    default_message = "Bad request"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)
