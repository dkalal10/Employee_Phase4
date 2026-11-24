
from fastapi import FastAPI

from database.connection import Base, engine
from routers.employee_routers import router as employee_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="Employee Management API",
    description="FastAPI application using layered architecture",
    version="1.0.0"
)

# Register employee router
app.include_router(employee_router)


@app.get("/")
def home():

    return {
        "message": "Welcome to Employee Management API"
    }


