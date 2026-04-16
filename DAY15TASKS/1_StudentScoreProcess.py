import math
students = [("Ram", 45), ("Sita", 78), ("John", 60), ("Anu", 30)]
student_dict = dict(students)
above_50 = {}
for name, marks in student_dict.items():
    if marks > 50:
        above_50[name] = marks
total = sum(student_dict.values())
avg = total / len(student_dict)
avg = math.floor(avg)  
with open("results.txt", "w") as file:
    file.write("Students above 50:\n")
    for name, marks in above_50.items():
        file.write(f"{name}: {marks}\n")
    
    file.write(f"\nAverage Marks: {avg}")

print("Done")
