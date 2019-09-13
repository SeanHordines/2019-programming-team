z = 0
n = int(input())
while(n != 0):
    z += 1
    map1 = [[0 for q in range(200)] for p in range(200)]

    for i in range(n):
        x, y, w, h = map(int, input().split())

        for a in range(w):
            for b in range(h):
                map1[x+a][y+b] = i+1

    print("Desktop " + str(z) + ":")

    for row in map1:
        line = ""
        for num in row:
            line += str(num)
        print(line)

    m = int(input())
    for i in range(m):
        x, y = map(int, input().split())
        if(map1[x][y] == 0):
            print("background")
        else:
            print("window " + str(map1[x][y]))

    n = int(input())
