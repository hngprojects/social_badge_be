from sqlalchemy.orm import Session
from sqlalchemy import select, func
from api.v2.models.platform_template import PlatformTemplate
from api.v2.schemas.layout import LayoutResponse, PaginatedLayouts


def list_layouts(
    db: Session,
    page: int = 1,
    limit: int = 10
) -> PaginatedLayouts:

    offset = (page - 1) * limit

    total = db.scalar(
        select(func.count()).select_from(PlatformTemplate)
        .where(PlatformTemplate.is_active == True)
    )

    templates = (
        db.execute(
            select(PlatformTemplate)
            .where(PlatformTemplate.is_active == True)
            .order_by(PlatformTemplate.name)
            .offset(offset)
            .limit(limit)
        )
        .scalars()
        .all()
    )

    layouts = [
        LayoutResponse(
            layout_id=template.id,
            name=template.name,
            description=template.description,
            thumbnail_url=template.thumbnail_url,
        )
        for template in templates
    ]

    return PaginatedLayouts(
        page=page,
        limit=limit,
        total=total,
        layouts=layouts
    )