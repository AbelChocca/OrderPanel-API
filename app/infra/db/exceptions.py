from app.infra.shared.infra_exception import InfraestructureException

class DatabaseException(InfraestructureException):
    def __init__(self, message: str, status_code = 500):
        super().__init__(message, status_code)

class ModelNotFound(InfraestructureException):
    def __init__(self, message: str, status_code = 404):
        super().__init__(message, status_code)