# def remove_dups(L):
#     new_list=[]
#     for number in L:
#         if number not in new_list:
#             new_list.append(number)
#     new_list.sort()
#     return new_list
# print(sorted(remove_dups([1,2,2,3,4,3])))

# def intersection(L1, L2):
#     new_list=[]
#     for number in remove_dups(L1):
#         if number in remove_dups(L2):
#             new_list.append(number)
#     return new_list
# def coauthors_dict():
# #     coauthors = {}
# file=open("CA-GrQc.csv","r")
# for line in file:
#     index=line.split(",")
#     print(index[0])
#         while index[0]!=index[1]:
#             list+=[index[1]]
#     # coauthors[index[0]]=list
#     # return coauthors
# coauthors_dict()
# print(coauthors_dict()[str(45)])

def coauthors_dict():
    coauthors = {}
    file=open("CA-GrQc.csv","r")
    for line in file:
        if line[0]!="#":
            index=line.split(",")
            # print(index[0],index[1])
            if index[0]!=index[1]:
                a=index[0]
                b=index[1]
                if coauthors.get(index[0],False):
                    list.append(int(b[1:4]))
                else:
                    list=[]
                    list.append(int(b[:5]))
                coauthors[int(a)]= list

print(coauthors_dict()[26])