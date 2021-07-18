def even_odd(L):
    index=0
    while index<len(L):
        if L[index]%2==0 and index>0:
            index1=index
            for a in range(index1):
                L[index1-1],L[index1]=L[index1],L[index1-1]
                index1-=1
        index+=1
    return L


def even_odd_fast(L):
    b=0
    e=-1
    beg=L[b]
    end=L[e]
    while beg<end:
        if beg%2==0:
            b+=1
            beg = L[b]
        if end%2==1:
            e-=1
            end = L[e]
        if beg%2==1 and end%2==0:
            L[b],L[e]=L[e],L[b]
            b+=1
            e-=1
            beg = L[b]
            end = L[e]
    return L
print(even_odd_fast([1,2,3,4,5,6,7,8,9]))
