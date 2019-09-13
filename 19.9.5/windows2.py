class rect:
    def __init__(x, y, w, h):
        this.x1 = x
        this.y1 = y
        this.x2 = x + w
        this.y2 = y + h

    def check(a, b):
        if((a >= this.x1 and a <= this.x2) and (b >= this.y1 and b <= this.y2)):
            return True
        return False

z = 0
N = int(input())
while(N != 0):
    z += 1
    windows = []

    for n in range(N):
        windows.append(rect(map(int, input().split())))

    M = int(input())
    print("Desktop " + z + ":")

    for m in range(M):
        x, y = map(int, input().split())
        index = -1
        for i in range(len(windows), 0, -1):
            if(windows[i].check(x, y)):
                index = i
                break
        print("Window " + index)
