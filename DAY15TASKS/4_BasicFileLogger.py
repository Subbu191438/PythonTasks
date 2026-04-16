while True:
    try:
        log = input("Enter log (type 'exit' to stop): ")
        
        if log.lower() == "exit":
            break
        
        with open("log.txt", "a") as file:
            file.write(log + "\n")
    
    except IOError:
        print("File error occurred!")
    except Exception:
        print("Something went wrong!")

print("Logging completed.")
