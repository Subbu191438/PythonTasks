employees=[]
with open("employee.txt","r")as file:
 for line in file:
    name,salary=line.split()
    salary=int(salary)
    employees.append((name,salary))
    print("Employee Details:\n")
    for emp in employees:
        print(emp[0],emp[1])
    if employees:
        highest=employees[0]
    for emp in employees:
        if emp[1]>highest[1]:
            highest=emp
            print("\nHighest Salary:")
            print(highest[0],highest[1])
    name=input("\nEnter new employee name:")
    salary=int(input("enter salary:"))
    with open("employee.txt","a")as file:
        file.write(name+""+str(salary)+"\n")
        print("New employee added successfully.")
                  
    
