# def insert(L,k):
#     unsorted_start = 0
#     while unsorted_start != len(L[0:k+1]):
#         for i in range(unsorted_start, len(L[0:k+1])):
#             if L[0:k+1][i] < L[0:k+1][unsorted_start]:
#                 L[unsorted_start], L[i] = L[i], L[unsorted_start]
#         unsorted_start += 1
#     return L
# L = [1, 3, 7, 2, 7, 9, 5, 4, 8]
# print(insert(L, 3))
#
# def comb_sort(L, k):
#     start = 0
#     while start != len(L):
#         for i in range(start, len(L[0:])):
#             if L[0:][i] < L[0:][start]:
#                 L[start], L[i] = L[i], L[start]
#         start += 1
#     return L
