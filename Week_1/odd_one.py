# Write a function named odd_one (L) that accepts a list L as argument. Except for one element,
# all other elements in L are of the same data type. The function odd_one should return the data
# type of this odd element.
# For example, if L is equal to [1, 2, 3.4, 5, 10], then the function should return the string
# float. This is because the element 3.4 is the odd one here, all other elements are integers.

def odd_one(L):
    P={}
    for element in L:
        if type(element) not in P:
            P[type(element)]=0
        P[type(element)]+=1
    for keys, values in P.items():
        if values==1:
            return keys.__name__
    return "Invalid"

print(odd_one(eval(input().strip())))
