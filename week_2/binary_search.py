import sys
from .utils import random_list_generator, quicksort, time_elapsed

sys.setrecursionlimit(10**6)

@time_elapsed
def  binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

@time_elapsed
def binary_search_recursive(list, item):
    if list==[]:
        return -1
    m=len(list)//2
    if item == list[m]:
        return m
    
    if item < list[m]:
        return binary_search_recursive(list[:m], item)
    else:
        return binary_search_recursive(list[m:], item)

@time_elapsed 
def linear_search(list, item): 
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None



if __name__ == "__main__":
    my_list=random_list_generator(10**5)
    my_list=quicksort(my_list)
    
    

    
    