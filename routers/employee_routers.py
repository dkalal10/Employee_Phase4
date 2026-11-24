from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.connection import get_db
from services.employee_services import EmployeeService
from models.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

employee_service = EmployeeService()


# Create employee
@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    try:
        return employee_service.create_employee(db, employee)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get all employees
@router.get("/", response_model=List[EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):

    return employee_service.get_all_employees(db)


# Get employee by ID
@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    try:
        return employee_service.get_employee_by_id(
            db, employee_id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Update employee
@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):

    try:
        return employee_service.update_employee(
            db, employee_id, employee
        )
    except ValueError as e:
        status_code = 404 if str(e) == "Employee not found" else 400
        raise HTTPException(status_code=status_code, detail=str(e))


# Delete employee
@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    try:
        return employee_service.delete_employee(db, employee_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

