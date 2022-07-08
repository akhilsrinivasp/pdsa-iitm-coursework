from utils import random_list_generator

def merge (left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(mylist):
    if len(mylist) <= 1:
        return mylist
    else:
        mid = len(mylist) // 2
        left = merge_sort(mylist[:mid])
        right = merge_sort(mylist[mid:])
        return merge(left, right)
    
if __name__=="__main__":
    mylist=random_list_generator(15)
    print(mylist)
    import time
    start=time.perf_counter()
    print(merge_sort(mylist))
    print((time.perf_counter()-start)*1000000, "µs")