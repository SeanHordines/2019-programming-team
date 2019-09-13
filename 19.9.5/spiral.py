from math import hypot

for t in range(int(input())):
    x, y = 1, 0
    for n in range(int(input())-1):
        h = hypot(x, y)
        x, y = x-y/h, x+y/h

    print(x, y)
