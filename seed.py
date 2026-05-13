from api.v1.models import *
from api.v1.models.associations import Base
from api.v1.services.user import user_service
from api.db.database import create_database, get_db
from api.v2.models.platform_template import PlatformTemplate

# create_database()
db = next(get_db())

# Seed admin user
admin_user = User(
    email="Isaacj@gmail.com",
    password=user_service.hash_password("45@&tuTU"),
    first_name="Isaac",
    last_name="John",
    is_active=True,
    is_superadmin=True,
    is_deleted=False,
    is_verified=True,
)
db.add(admin_user)


# Seed 4 layout records
layouts = [
    PlatformTemplate(
        name="Classic",
        description="A clean, timeless badge layout suitable for all events.",
        thumbnail_url="https://example.com/thumbnails/classic.png",
        is_active=True,
    ),
    PlatformTemplate(
        name="Modern",
        description="A sleek, contemporary design with bold typography.",
        thumbnail_url="https://example.com/thumbnails/modern.png",
        is_active=True,
    ),
    PlatformTemplate(
        name="Minimal",
        description="A stripped-back layout that puts the focus on essentials.",
        thumbnail_url="https://example.com/thumbnails/minimal.png",
        is_active=True,
    ),
    PlatformTemplate(
        name="Bold",
        description="A vibrant, high-contrast layout designed to stand out.",
        thumbnail_url="https://example.com/thumbnails/bold.png",
        is_active=True,
    ),
]

for layout in layouts:
    db.add(layout)

db.commit()
print("Seed data successfully inserted")