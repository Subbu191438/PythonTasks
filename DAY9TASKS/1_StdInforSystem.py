class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print()
s1 = Student("Rahul", 1, 85)
s2 = Student("Anita", 2, 90)
s3 = Student("Ravi", 3, 78)
s1.display()
s2.display()
s3.display()
