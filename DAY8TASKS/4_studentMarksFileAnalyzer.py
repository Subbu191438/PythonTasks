# Program to Analyze Marks
try:
    total_marks = 0
    count = 0
 
    # 1. Read the file
    with open("marks.txt", "r") as file:
        print("Student Records:")
        for line in file:
            # 2. Display student records
            name, marks = line.split()
            marks = int(marks)
            print(f"{name}: {marks}")
 
            # Prepare for average
            total_marks += marks
            count += 1
 
    # 3. Calculate and display average
    if count > 0:
        average = total_marks / count
        print(f"\nAverage Marks: {average}")
    else:
        print("File is empty.")
 
except FileNotFoundError:
    print("Error: marks.txt not found. Please create the file first.")
