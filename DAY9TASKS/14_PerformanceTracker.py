import time
def time_tracker(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start, "seconds")
        return result
    return wrapper
@time_tracker
def sample_task():
    for i in range(1000000):
        pass
sample_task()
