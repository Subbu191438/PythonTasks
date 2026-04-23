# Take student name as input
name = input("Enter student name: ")

# Append name to file
with open("attendance.txt", "a") as file:
    file.write(name + "\n")

# Display file contents
with open("attendance.txt", "r") as file:
    print("\nAttendance Record:")
    print(file.read())