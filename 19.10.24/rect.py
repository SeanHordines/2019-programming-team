rects = []

for n in range(int(input())):
    rects.append(tuple(map(int, input().split())))

area = 0
asddFSA = 0

found = {}

for i in range(len(rects)):
    x1, y1, x2, y2 = rects[i]
    for x in range(x1, x2):
        for y in range(y1, y2):
            temp = "" + str(x) + ", " + str(y)
            try:
                if found[temp] == 1:
                    continue
            except KeyError:
                asddFSA += 1
                #print("already checked")
            valid = 1
            for j in range(i+1, len(rects)):
                a, b, c, d = rects[j]
                if((a <= x <= b) and (c <= y <= d)):
                    valid *= -1
            if valid == 1:
                area += 1
            found[temp] = 1

print(area)
print(asddFSA)
