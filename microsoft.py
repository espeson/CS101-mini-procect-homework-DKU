def solution(N):
    N=str(N)
    sun_1=0
    sun_2=0
    list=[]
    for num in N:
        sun_1+=int(num)
    for number in range(1000000):
        numb=str(number)
        for num in numb:
            sun_2+=int(num)
            if sun_2==2*sun_1 and number > int(N):
                return number
print(solution(14))