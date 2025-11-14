class ZapierError(Exception):
    """class representing Generic Http error."""

    def __init__(self, message=None, response=None):
        super().__init__(message)
        self.message = message
        self.response = response


class ZapierBackoffError(ZapierError):
    """class representing backoff error handling."""
    pass

class ZapierBadRequestError(ZapierError):
    """class representing 400 status code."""
    pass

class ZapierUnauthorizedError(ZapierError):
    """class representing 401 status code."""
    pass


class ZapierForbiddenError(ZapierError):
    """class representing 403 status code."""
    pass

class ZapierNotFoundError(ZapierError):
    """class representing 404 status code."""
    pass

class ZapierConflictError(ZapierError):
    """class representing 409 status code."""
    pass

class ZapierUnprocessableEntityError(ZapierBackoffError):
    """class representing 422 status code."""
    pass

class ZapierRateLimitError(ZapierBackoffError):
    """class representing 429 status code."""
    pass

class ZapierInternalServerError(ZapierBackoffError):
    """class representing 500 status code."""
    pass

class ZapierNotImplementedError(ZapierBackoffError):
    """class representing 501 status code."""
    pass

class ZapierBadGatewayError(ZapierBackoffError):
    """class representing 502 status code."""
    pass

class ZapierServiceUnavailableError(ZapierBackoffError):
    """class representing 503 status code."""
    pass

ERROR_CODE_EXCEPTION_MAPPING = {
    400: {
        "raise_exception": ZapierBadRequestError,
        "message": "A validation exception has occurred."
    },
    401: {
        "raise_exception": ZapierUnauthorizedError,
        "message": "The access token provided is expired, revoked, malformed or invalid for other reasons."
    },
    403: {
        "raise_exception": ZapierForbiddenError,
        "message": "You are missing the following required scopes: read"
    },
    404: {
        "raise_exception": ZapierNotFoundError,
        "message": "The resource you have specified cannot be found."
    },
    409: {
        "raise_exception": ZapierConflictError,
        "message": "The API request cannot be completed because the requested operation would conflict with an existing item."
    },
    422: {
        "raise_exception": ZapierUnprocessableEntityError,
        "message": "The request content itself is not processable by the server."
    },
    429: {
        "raise_exception": ZapierRateLimitError,
        "message": "The API rate limit for your organisation/application pairing has been exceeded."
    },
    500: {
        "raise_exception": ZapierInternalServerError,
        "message": "The server encountered an unexpected condition which prevented" \
            " it from fulfilling the request."
    },
    501: {
        "raise_exception": ZapierNotImplementedError,
        "message": "The server does not support the functionality required to fulfill the request."
    },
    502: {
        "raise_exception": ZapierBadGatewayError,
        "message": "Server received an invalid response."
    },
    503: {
        "raise_exception": ZapierServiceUnavailableError,
        "message": "API service is currently unavailable."
    }
}

