from fastapi import APIRouter
from api.v2.routes.layout import layout

api_version_two = APIRouter(prefix="/api/v2")

api_version_two.include_router(layout)