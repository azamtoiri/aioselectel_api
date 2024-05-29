class SelectelError(Exception):
    pass


class SelectelAuthError(SelectelError):
    pass


class SelectelRequestError(SelectelError):
    pass


class AuthError(Exception):
    """Exception raised for errors during authentication."""
    pass


class RequestError(Exception):
    """Exception raised for errors during HTTP requests."""
    pass
