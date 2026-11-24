from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional

from database.connection import Base


# SQLAlchemy database model
class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    department = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)


# Pydantic schema for creating an employee
class EmployeeCreate(BaseModel):

    name: str
    email: EmailStr
    department: str
    salary: float


# Pydantic schema for updating an employee
class EmployeeUpdate(BaseModel):

    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    salary: Optional[float] = None


# Pydantic schema for API response
class EmployeeResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    department: str
    salary: float

    model_config = ConfigDict(from_attributes=True)


