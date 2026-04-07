name = input("Enter student name: ")
with open("attendance.txt", "a") as file:
    file.write(name + "\n")
print("\nAttendance Record:")
with open("attendance.txt", "r") as file:
    for line in file:
        print(line.strip())
