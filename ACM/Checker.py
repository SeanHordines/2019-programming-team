r, c, v, h = map(int, input().split())
board = [[0 for j in range(v)] for i in range(h)]
a = [int(input()) for i in range(v)]
b = [int(input()) for j in range(h)]

borw = "B"

for i in range(v):
    for j in range(h):
        
        board[i][j] = [[borw for k in range(a[i])] for l in range(b[j])]
    if (borw == "B"):
        borw = "W"
    else:
        borw = "B"

for i in range(v):
    print(board[i])
