class BaseAppError(Exception):
    """Classe base para erros da aplicação."""

    error_type = "APP_ERROR"

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def to_dict(self):
        return {
            "error": {
                "type": self.error_type,
                "message": self.message
            }
        }


class BusinessError(BaseAppError):
    error_type = "BUSINESS_ERROR"


class ResourceNotFoundError(BusinessError):
    error_type = "RESOURCE_NOT_FOUND"


class ExternalAPIError(BaseAppError):
    error_type = "EXTERNAL_API_ERROR"
