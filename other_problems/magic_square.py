n, k = map(int, input().split())
grid = []

def printGrid(g):
    for row in g:
        print(row)

def isValid(g):
    valid = True

    #check rows
    tot = sum(g[0])
    for row in g:
        temp = sum(row)
        #print(temp)
        if(temp != tot):
            valid = False

    #check columns
    for i in range(n):
        temp = 0
        for j in range(n):
            temp += grid[j][i]
        #print(temp)
        if(temp != tot):
            valid = False

    return valid


for _ in range(n):
    grid.append([int(x) for x in input().split()])

#printGrid(grid)
#print(isValid(grid))
