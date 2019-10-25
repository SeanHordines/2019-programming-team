from math import hypot

x, y, x1, y1, x2, y2 = map(int, input().split())

dist = 0

if(x <= x1):
    if(y <= y1):
        dist = hypot(x-x1, y-y1)
    elif(y2 <= y):
        dist = hypot(x-x1, y-y2)
    else:
        dist = abs(x-x1)
elif(x2 <= x):
    if(y <= y1):
        dist = hypot(x-x2, y-y1)
    elif(y2 <= y):
        dist = hypot(x-x2, y-y2)
    else:
        dist = abs(x-x2)
else:
    if(y <= y1):
        dist = abs(y-y1)
    elif(y2 <= y):
        dist = abs(y-y2)
    else:
        pass

print("%.3f" % dist)
