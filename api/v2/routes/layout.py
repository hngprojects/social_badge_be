from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.v1.models.user import User
from api.v1.services.user import user_service
from api.utils.success_response import success_response
from api.v2.services.layout_service import list_layouts

layout = APIRouter(prefix="/layouts", tags=["Layouts"])

@layout.get("", status_code=status.HTTP_200_OK)
def get_layouts(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(user_service.get_current_user),
):
    layouts = list_layouts(db, page, limit)
    return success_response(
    status_code=status.HTTP_200_OK,
    message="Layouts retrieved successfully",
    data=layouts.model_dump(),
)