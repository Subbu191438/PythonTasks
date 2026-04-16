import numpy as np
import pandas as pd
import time
def read_numbers(file_name):
    try:
        with open(file_name, "r") as file:
            for line in file:
                try:
                    yield float(line.strip())  
                except:
                    print("Invalid data skipped:", line.strip())
    except FileNotFoundError:
        print("File not found!")
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start)
        return result
    return wrapper
@timer
def process_data(file_name):
    data = list(read_numbers(file_name)) 
    
    if len(data) == 0:
        print("No valid data")
        return
    mean = np.mean(data)
    std = np.std(data)
    df = pd.DataFrame({
        "Mean": [mean],
        "Std Dev": [std]
    })
    
    return df
result = process_data("data.txt")
if result is not None:
    print(result)
