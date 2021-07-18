student1 = 'student1@dukekunshan.edu.cn,23'
student2 = 'student2@dku,16'
student3 = '17,student3@DKU'
student4 = 'student4@dukekunshan.edu.cn,29'
student5 = 'student5@dku,16'
student6 = '19,student6@DKU'
student7 = 'student7@dukekunshan.edu.cn,28'
student8 = 'student8@dku,27'
student9 = '17,student9@DKU'
#
# def get_age(student):
#     a = 0
#     while a < len(student):
#         if student[a] == ",":
#             break
#         a += 1
#     if student[a - 1] in "1234567890":
#         return student[a - 2:a]
#     if student[a + 1] in "1234567890":
#         return student[a + 1:a + 3]
# print(get_age(student3))
def get_email(student):
    b=0
    d=-1
    while b<len(student):
        if student[b]==",":
            d=b
        if student[b] =="@":
            break
        b+=1
    return student[b:]
# def standardize(student):
#     g=""
#     h=get_age(student)
#     if int(h)>18:
#         h="**"
#     f=get_email(student),",",h
#     for letter in f:
#         if letter not in "":
#             g+=letter
#     return g
# print(standardize(student1))


# print(get_email(student))
# def standardize(student):
#     return get_email(student),get_age(student)
# print(standardize(student))
print(get_email(student1))