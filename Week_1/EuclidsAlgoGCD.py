from ast import Call
import time

def timer(func):
    def wrapper(*args, **kwargs):
        mrts = time.time()
        res = func(*args, **kwargs)
        print("Time Taken to run the function {}: ".format(func.__name__), (time.time() - mrts) *1000000, "µs")
        return res
        
    return wrapper

# @timer
def ToOptimiseGCD(a, b):
    (a, b) = (max(a,b), min(a,b))
    if a%b == 0: 
        return b
    else: 
        return ToOptimiseGCD(b, a-b)

# @timer
def EuclidianAlgo(a,b):
    (a, b) = (max(a,b), min(a,b))
    if a%b == 0: 
        return b
    else: 
        return ToOptimiseGCD(b, a%b)
    
@timer
def CallEuclidianAlgo(a,b): #Separate function due to the presence of recursion 
    return EuclidianAlgo(a,b)

@timer
def CallToOptimiseGCD(a,b):
    return ToOptimiseGCD(a,b)

print("GCD: ", CallToOptimiseGCD(20000000, 100000000))

print("Euclidian GCD: ", CallEuclidianAlgo(20000000, 100000000))




