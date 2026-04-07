try:
    with open("notes.txt", "r") as file:
        content = file.read()  
        
    print("Contents of notes.txt:\n")
    print(content)

except FileNotFoundError:
    print("The file 'notes.txt' does not exist.")
except Exception as e:
    print("An error occurred:", e)
