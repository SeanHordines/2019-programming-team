#mercer d team
#room 251

r, c, v, h = map(int, input().split())

vertical = [0]
horizontal = [0]

for i in range(v):
    vertical.append(int(input()) + vertical[-1])

for i in range(h):
    horizontal.append(int(input()) + horizontal[-1])

def find(L, val):
    loc = 1
    while(val >= L[loc]):
        loc += 1
    return loc




for i in range(r):
    string = ""
    for j in range(c):
        bORw = find(vertical, i) + find(horizontal, j)
        if(bORw % 2 == 0):
            string += "B"
        else:
            string += "W"
    print(string)
