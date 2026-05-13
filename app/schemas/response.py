from pydantic import BaseModel


class SuccessResponse[DataT](BaseModel):
    """Standardized success response envelope returned by all endpoints."""

    status: str = "success"
    message: str
    data: DataT | None = None


class ErrorResponse(BaseModel):
    """Standardized error response envelope returned on all failures."""

    status: str = "error"
    message: str
