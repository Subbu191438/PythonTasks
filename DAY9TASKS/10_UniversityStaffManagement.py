class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Professor(Staff):
    def display(self):
        print("Professor Name:", self.name)
        print("Salary:", self.salary)

class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant Name:", self.name)
        print("Salary:", self.salary)

class Administrator(Staff):
    def display(self):
        print("Administrator Name:", self.name)
        print("Salary:", self.salary)
p = Professor("Dr. Rao", 80000)
l = LabAssistant("Suresh", 30000)
a = Administrator("Meena", 40000)
p.display()
l.display()
a.display()
