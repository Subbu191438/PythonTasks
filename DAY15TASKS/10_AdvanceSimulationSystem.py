import random
import numpy as np
import pandas as pd
import math
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.marks >= 75:
            return "A"
        elif self.marks >= 50:
            return "B"
        else:
            return "C"
names = ["A", "B", "C", "D", "E"]
marks_list = [random.randint(0, 100) for _ in range(len(names))]
marks_array = np.array(marks_list)
students = []
for i in range(len(names)):
    students.append(Student(names[i], marks_array[i]))
data = {
    "Name": [s.name for s in students],
    "Marks": [s.marks for s in students],
    "Grade": [s.grade for s in students]
}
df = pd.DataFrame(data)
mean = np.mean(marks_array)
std = np.std(marks_array)
floor_mean = math.floor(mean)
try:
    with open("report.txt", "w") as file:
        file.write(df.to_string(index=False))
        file.write(f"\n\nMean: {mean}")
        file.write(f"\nStd Dev: {std}")
        file.write(f"\nFloor Mean: {floor_mean}")
except:
    print("File error!")
print(df)
print("\nMean:", mean)
print("Std Dev:", std)
print("Floor Mean:", floor_mean)
