import time

def timer(func):
    def wrapper(*args, **kwargs):
        mrts = time.perf_counter()
        res = func(*args, **kwargs)
        print("Time Taken to run the function {}: ".format(func.__name__), (time.perf_counter() - mrts) *1000000, "µs")
        return res
        
    return wrapper