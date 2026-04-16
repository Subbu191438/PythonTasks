class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        return f"{self.emp_id} - {self.name} - {self.salary}"
employees = {}
for i in range(3):
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    
    try:
        salary = float(input("Enter Salary: "))
        emp = Employee(emp_id, name, salary)
        employees[emp_id] = emp
    except:
        print("Invalid salary! Skipping employee.")
try:
    with open("employees.txt", "w") as file:
        for emp in employees.values():
            file.write(emp.display() + "\n")
except:
    print("File error!")
print("\nEmployee List:")
for emp in employees.values():
    print(emp.display())
