# Finding Twin primes
import time
def prime(n): # efficient way to check if a number is prime
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def twin_primes(n, m): 
    l = []
    for i in range(n, m+1):
        if prime(i) and prime(i+2):
            l.append((i, i+2)) 
    return l

n=input("Enter the starting number: ")
m=input("Enter the ending number: ")
begin=time.perf_counter()
print(twin_primes(int(n), int(m)))
end=time.perf_counter()
print("Time taken: ", (end-begin)*1000000, "µs")