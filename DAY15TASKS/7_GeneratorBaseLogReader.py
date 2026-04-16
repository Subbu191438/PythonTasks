def read_logs(file_name):
    try:
        with open(file_name, "r") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print("File not found!")
error_count = {}
for line in read_logs("log.txt"):
    if line and "ERROR" in line:  
        error_count[line] = error_count.get(line, 0) + 1
print("Error occurrences:")
for error, count in error_count.items():
    print(error, ":", count)
