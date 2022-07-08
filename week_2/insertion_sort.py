from utils import random_list_generator
import time

def insertion_sort(ml):
    n=len(ml)
    for i in range(1, n):
        j=i
        while j>0 and ml[j-1]>ml[j]:
            ml[j-1], ml[j]=ml[j], ml[j-1]
            j-=1
    return ml

def insert(ml,v):
    n=len(ml)
    if n==0:
        return [v]
    if v >= ml[-1]:
        return ml+[v]
    else:
        return insert(ml[:-1], v)+ml[-1:]
    
def insertion_sort_recursive(ml):
    n=len(ml)
    if n < 1:
        return ml
    ml = insert(insertion_sort_recursive(ml[:-1]), ml[-1])
    return ml    

if __name__=="__main__":
    ml=random_list_generator(10)
    start=time.perf_counter()
    print(insertion_sort(ml))
    end=time.perf_counter()
    print((end-start)*1000000, "µs")
    
    start=time.perf_counter()
    print(insertion_sort_recursive(ml))
    end=time.perf_counter()
    print((end-start)*1000000, "µs")