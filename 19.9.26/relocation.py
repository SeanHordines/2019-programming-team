N, Q = map(int, input().split())
line = [int(x) for x in input().split()]

dict = {}
comp = 1
for loc in line:
    dict[comp] = loc
    comp += 1

for i in range(Q):
    temp = [int(x) for x in input().split()]
    if(temp[0] == 1):
        dict[temp[1]] = temp[2]
    elif(temp[0] == 2):
        a = dict[temp[1]]
        b = dict[temp[2]]
        print(abs(a-b))
