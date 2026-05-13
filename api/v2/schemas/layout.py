from pydantic import BaseModel, Field


class LayoutResponse(BaseModel):
    """Layout option returned to organisers for template selection."""

    layout_id: str = Field(..., description="Stable layout identifier", examples=["classic"])
    name: str = Field(..., description="Human-readable layout name")
    description: str = Field(..., description="Short description shown in UI")
    thumbnail_url: str = Field(..., description="Public URL for layout preview artwork",)

class PaginatedLayouts(BaseModel):
    page: int
    limit: int
    total: int
    layouts: list[LayoutResponse]