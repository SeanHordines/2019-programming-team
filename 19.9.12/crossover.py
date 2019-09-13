line = [int(x) for x in input().split()]
c = 1
while(len(line) != 0):
    crosses = 0
    for i in range(len(line)):
        pin = line[i]
        for j in range(i+1, len(line)):
            if(line[j] < pin):
                crosses+=1
    print("There are", crosses, "wire crossings in routing channel", c)
    line = [int(x) for x in input().split()]
    c+=1
