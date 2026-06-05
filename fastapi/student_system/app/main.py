from fastapi import FastAPI

from app.routers import student
from app.database import engine
from app.models import Base

# Create tables
Base.metadata.create_all(bind=engine)

# Create ONE FastAPI instance
app = FastAPI(
    title="Student System API",
    description="A professional student management system",
    version="1.0.0"
)

# Register routers
app.include_router(student.router)