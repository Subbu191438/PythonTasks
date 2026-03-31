subjects = ("Math", "Science", "English")
student_names = set()
students = {}
def calculate_total(marks):
    if len(marks) == 0:
        return 0
    return marks[0] + calculate_total(marks[1:])
def add_student():
    name = input("Enter student name: ")
    student_names.add(name)
    
    marks = []
    try:
        for sub in subjects:
            m = int(input(f"Enter marks for {sub}: "))
            marks.append(m)
        students[name] = marks
    except ValueError:
        print("Invalid input! Please enter numeric marks.")
def display_students():
    for name, marks in students.items():
        print(f"{name}: {marks}")
def calculate_average():
    name = input("Enter student name to calculate average: ")
    
    try:
        if name not in students:
            raise NameError
        
        marks = students[name]
        
        if not isinstance(marks, list):
            raise TypeError
        
        total = calculate_total(marks)
        avg = total / len(marks)
        
        print("Total Marks:", total)
        print("Average Marks:", avg)
    
    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Marks data type error.")
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        calculate_average()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
