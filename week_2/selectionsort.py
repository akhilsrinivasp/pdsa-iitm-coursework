from utils import random_list_generator

def selection_sort(mylist): 
    n=len(mylist)
    if n<0:
        return mylist
    for i in range(n):
        minpos=i
        for j in range(i+1, n):
            if mylist[j]<mylist[minpos]:
                minpos=j
        mylist[i], mylist[minpos]=mylist[minpos], mylist[i]
    return mylist

if __name__=="__main__":
    mylist=random_list_generator(10000)
    print(mylist)
    import time
    start=time.perf_counter()
    print(selection_sort(mylist))
    print((time.perf_counter()-start)*1000000, "µs")
    