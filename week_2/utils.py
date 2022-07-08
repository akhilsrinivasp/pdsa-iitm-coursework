def random_list_generator(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(0, n))
    return l

def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

import time

def time_elapsed(func):
    def wrapper(*args, **kwargs):
        mrts = time.perf_counter()
        res = func(*args, **kwargs)
        print("Time Taken to run the function {}: ".format(func.__name__), (time.perf_counter() - mrts) *1000000, "µs")
        return res
    return wrapper