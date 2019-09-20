lines = []

for i in range(int(input())):
    lines.append(input()[::-1])

lines.sort()
for l in lines:
    print(l)
