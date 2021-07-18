def merge(L1, L2):
    L=[]
    for ele in L1:
        L.append(ele)
    for ele in L2:
        L.append(ele)

    return sorted(L)


def merge_sort(L):
    index=(len(L)-1)//2
    if index==0 or index==1:
        return L
    else:
        return merge(L[:index],L[index:])
print(merge_sort([4, 2, 1, 9, 3, 9, 2, 3, 5, 6, 3, 4, 9, 11]))