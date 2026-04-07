def add_bonus(func):
    def wrapper(self):
        bonus_salary = self.salary + (self.salary * 0.10)  # 10% bonus
        print("Salary with Bonus:", bonus_salary)
    return wrapper

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @add_bonus
    def display_salary(self):
        print("Salary:", self.salary)
e = Employee("Ravi", 50000)
e.display_salary()
