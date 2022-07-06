## this problem is based on the Goldbach's conjecture. It is a conjecture that every even 
## number greater than 2 can be written as the sum of two prime numbers.

def prime(n): # efficient way to check if a number is prime
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def Goldbach(n):
    l = []
    for i in range(2, (n//2)+1):
        if prime(i) and prime(n-i):
            l.append((i, n-i))
    return l

print(Goldbach(int(input("Enter the number: "))))