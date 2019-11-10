# mercer binary bears team d
# room 251

w = int(input())

list = []
for i in range(w):
    list.append(int(input()))

min = -1

for i in range(len(list)):
    count = list.count(list[i])

    sum1, sum2, = 0, 0

    if (count == 1):
        for j in range(len(list)):
            if(list[j] <= list[i]):
                sum1 += list[j]
            else:
                sum2 += list[j]

        if(sum1 == sum2):
            min = list[i]+1
        elif(sum1 - list[i] == sum2):
            min = list[i]
    else:
        for j in range(len(list)):
            if(list[j] < list[i]):
                sum1 += list[j]
            elif(list[j] > list[i]):
                sum2 += list[j]

        if(sum1 == sum2):
            min = list[i]

print(min)
