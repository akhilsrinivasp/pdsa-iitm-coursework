import time

def timer(func):
    def wrapper(*args, **kwargs):
        mrts = time.perf_counter()
        res = func(*args, **kwargs)
        print("Time Taken to run the function {}: ".format(func.__name__), (time.perf_counter() - mrts) *1000000, "µs")
        return res
        
    return wrapper

@timer
def ToOptimiseGCD(a,b):
    def func(a, b):
        (a, b) = (max(a,b), min(a,b))
        if a%b == 0: 
            return b
        else: 
            return func(b, a-b)
    return func(a,b)

@timer
def EuclidianAlgo(a,b):
    def func(a, b):
        if a%b == 0: 
            return b
        else: 
            return func(b, a%b)
    return func(a,b)

print("GCD: ", ToOptimiseGCD(12, 24))
print("Euclidian GCD: ", EuclidianAlgo(12, 24))




