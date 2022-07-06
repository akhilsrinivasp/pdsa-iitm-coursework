import time
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

def linear_search(list, item): 
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None

def random_list_generator(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(0, n))
    return l

if __name__ == "__main__":
    my_list=random_list_generator(100000)
    start=time.perf_counter()
    print(binary_search(my_list, 30))
    end=time.perf_counter()
    print("Time taken: ", (end-start)*1000000, "µs")
    
    start=time.perf_counter() 
    print(linear_search(my_list, 30)) 
    end=time.perf_counter()
    print("Time taken: ", (end-start)*1000000, "µs")
    