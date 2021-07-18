# def num_coauthors(author):
#     text=open("CA-GrQc.csv","r")
#     count=0
#     for line in text:
#         if line[0]!="#":
#             index=line.split(",")
#             for writer in index:
#                 if writer == str(author):
#                     count+=1
#     return count
# print(num_coauthors(25443))

# def get_people(family_initial):
#     person=""
#     text=open("people.csv","r")
#     for line in text:
#         if line[0]!="#":
#             index=line.split(",")
#             for people in index[1]:
#                 if people[0] == family_initial.upper():
#                     person+=index[1]+", "+index[0]+"\n"
#     return person[:-1]
# print('Zane, Sheridan\nZurcher, Jerry\nZepp, Vincenza\nZagen, Serina'==get_people("z"))
# print(len('Zane, Sheridan\nZurcher, Jerry\nZepp, Vincenza\nZagen, Serina'))
# print(len(get_people("z")))

#
# text = open("people_semicolon.csv", "r")
# text1 = open("people_semicolon.csv", "r")
# birthdate = ""
# memory = ()
# for line in text:
#     if line[0] != "#":
#         birthdate += ((line.split(";")[-1]))
# index = birthdate.split("\n")
# for element in index:
#     indexpro = element.split("/")
#     if len(indexpro[1]) < 2:
#         indexpro[1] = "0" + indexpro[1]
#     if len(indexpro[0]) < 2:
#         indexpro[0] = "0" + indexpro[0]
#     age = indexpro[2] + indexpro[0] + indexpro[1]
#     memory += ((int(age)),)
# oldest = min(memory)
# for linepro in text1:
#     if "1/6/1970" in linepro:
#         text1 = linepro.split(";")
#         oldest_person = text1[1] + ", " + text1[0]
#         break
# print(len(oldest_person))
# exit()
