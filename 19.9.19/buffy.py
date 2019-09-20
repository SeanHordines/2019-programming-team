asdf = 1
temp = input()
while(temp != ""):
    n, m = map(int, temp.split())

    text = ""

    grid = []
    for i in range(n):
        grid.append([t for t in input().split()])
        text = text + grid[i][m-i-1] + " "

    print("Message", asdf, "=>", text)
    asdf += 1
    temp = input()
