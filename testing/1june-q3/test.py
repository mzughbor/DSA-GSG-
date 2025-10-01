from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    def __init__(self, name: str, emp_id: int, base_salary: float):
        self.name = name
        self.id = emp_id
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    @abstractmethod
    def get_benefits(self) -> str:
        pass


# Full Time Employee Subclass
class FullTimeEmployee(Employee):
    def __init__(self, name: str, emp_id: int, base_salary: float, bonus: float):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.base_salary + self.bonus

    def get_benefits(self) -> str:
        return "Full-time benefits"


# Part Time Employee Subclass
class PartTimeEmployee(Employee):
    def __init__(self, name: str, emp_id: int, hours_worked: float, hourly_rate: float):
        # base_salary is not used here, just set to 0
        super().__init__(name, emp_id, base_salary=0)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self) -> float:
        return self.hours_worked * self.hourly_rate

    def get_benefits(self) -> str:
        return "No benefits"


# Example Usage
if __name__ == "__main__":
    full_time = FullTimeEmployee("Alice", 101, 50000, 5000)
    part_time = PartTimeEmployee("Bob", 202, 80, 25)

    for emp in [full_time, part_time]:
        print(f"Name: {emp.name}")
        print(f"ID: {emp.id}")
        print(f"Salary: ${emp.calculate_salary():,.2f}")
        print(f"Benefits: {emp.get_benefits()}")
        print("-" * 30)
