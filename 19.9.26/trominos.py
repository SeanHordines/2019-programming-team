num = int(input())
lst = []
for a in range(num):
    b,c = input().split()
    b = int(b)
    c = int(c)
    lst.append(b)
    lst.append(c)

it = iter(lst)

for a,b in zip(it, it):
    x = a
    y = b
    if x%2 !=0 :
        x = x-1
    if y%2 !=0 :
        y = y-1

    #print(x,y)
    #print(x%3, x%6, y%3)
    #print(x%4, y%4)

    if x==y:
        print(0)
    elif(x == 0 and y %4 != 0):
        print(1)
    elif(y == 0 and x%4 == 0):
        print(0)
    elif(y == 0 and x%4 != 0):
        print(3)
    elif(y%4 == 0 and x%4 != 0 and x%3 != 0):
        print(1)
    elif(y%4 == 0 and x%4 == 0):
        print(0)
    elif(x%6 == 0 and y%3 == 0 and x%4 !=0):
        print(3)
    elif(x%3 != 0 and y%3 == 0):
        print(2)
    elif(x%3 == 0 and y%3 == 0 and y%4 != 0):
        print(1)
    else:
        print(2)
