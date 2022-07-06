def find_Min_Difference(L,P):
    L.sort()
    N=P
    M=len(L)
    min_value=max(L)-min(L)
    for i in range(M-N+1):
        if L[i+N-1]-L[i]<min_value:
            min_value=L[i+N-1]-L[i]
    return min_value
    
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))