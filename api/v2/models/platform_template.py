from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from api.v1.models.base_model import BaseTableModel


class PlatformTemplate(BaseTableModel):
    """Platform-owned badge template layouts."""

    __tablename__ = "platform_templates"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    thumbnail_url: Mapped[str] = mapped_column(String(512), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)