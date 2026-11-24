    
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from repositories.employee_repository import EmployeeRepository
from models.employee import EmployeeCreate, EmployeeUpdate


class EmployeeService:

    def __init__(self):

        self.repository = EmployeeRepository()

    # Create employee
    def create_employee(
        self,
        db: Session,
        employee: EmployeeCreate
    ):

        # Business validation
        if employee.salary <= 0:
            raise ValueError("Salary must be greater than zero")

        try:
            return self.repository.create_employee(db, employee)
        except IntegrityError:
            db.rollback()
            raise ValueError("Employee email already exists")

    # Get all employees
    def get_all_employees(self, db: Session):

        return self.repository.get_all_employees(db)

    # Get employee by ID
    def get_employee_by_id(
        self,
        db: Session,
        employee_id: int
    ):

        employee = self.repository.get_employee_by_id(
            db, employee_id
        )

        if not employee:
            raise ValueError("Employee not found")

        return employee

    # Update employee
    def update_employee(
        self,
        db: Session,
        employee_id: int,
        update_data: EmployeeUpdate
    ):

        employee = self.get_employee_by_id(db, employee_id)

        if update_data.salary is not None and update_data.salary <= 0:
            raise ValueError("Salary must be greater than zero")

        try:
            return self.repository.update_employee(
                db, employee, update_data
            )
        except IntegrityError:
            db.rollback()
            raise ValueError("Employee email already exists")

    # Delete employee
    def delete_employee(self, db: Session, employee_id: int):

        employee = self.get_employee_by_id(db, employee_id)

        self.repository.delete_employee(db, employee)

        return {"message": "Employee deleted successfully"}


