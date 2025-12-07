class BaseError(Exception):
    """
    Base class for all base exceptions.
    """

    status_code: int = 400

    def __init__(self, message: str, *, status_code: int | None = None):
        super().__init__(message)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
