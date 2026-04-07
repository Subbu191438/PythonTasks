with open("grocery.txt", "w") as file:
    print("Enter grocery items (type 'done' to stop):")
    
    while True:
        item = input("Enter item: ")
        
        if item.lower() == "done":
            break
        
        file.write(item + "\n")

print("Grocery items saved successfully.")
