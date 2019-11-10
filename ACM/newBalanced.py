# mercer binary bears team d
# room 251

w = int(input())

list = []
for i in range(w):
    list.append(int(input()))

min = -1

list.sort()

for i in range(w):
    # count = list.count(list[i])
    sum1, sum2, = 0, 0
    count = 1

    if(i == 0):
        if (list[i] == list[i+1]):
            count = 2
    elif (i == len(list)):
        if (list[i] == list[i-1]):
            count = 2
    elif (list[i] == list[i+1] or list[i] == list[i-1]):
        count = 2


    if (count == 1):
        for j in range(w):
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
