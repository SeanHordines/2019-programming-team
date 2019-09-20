width, height = map(int, input().split())

grid = []
for y in range(height):
    row = [float(x) for x in input().split()]
    grid.append(row)

for n in range(int(input())):
    row, col = map(int, input().split())
    dropSediment = 0.0
    moving = True
    while(moving):
        curr = grid[row][col]
        maxDif = 0.0
        dir = ""
        if(col-1 >= 0 and (curr - grid[row][col-1]) > maxDif):
            maxDif = (curr - grid[row][col-1])
            dir = "W"
        if(col+1 < width and (curr - grid[row][col+1]) > maxDif):
            maxDif = (curr - grid[row][col+1])
            dir = "E"
        if(row-1 >= 0 and (curr - grid[row-1][col]) > maxDif):
            maxDif = (curr - grid[row-1][col])
            dir = "N"
        if(row+1 < height and (curr - grid[row+1][col]) > maxDif):
            maxDif = (curr - grid[row+1][col])
            dir = "S"

        if(maxDif == 0.0):
            moving = False
            print(row, col, dropSediment)
            grid[row][col] += dropSediment
            break

        rateOfExchange = 0.8**(11-maxDif)
        deltaSediment = (1.0-dropSediment)*rateOfExchange
        #print(row, col, dir, deltaSediment)
        grid[row][col] -= deltaSediment
        dropSediment += deltaSediment
        if(dir == "W"):
            col -= 1
        elif(dir == "E"):
            col += 1
        elif(dir == "N"):
            row -= 1
        elif(dir == "S"):
            row += 1
        grid[row][col] += dropSediment*rateOfExchange
        dropSediment -= dropSediment*rateOfExchange

total = 0
for row in range(height):
    print(grid[row])
    for col in range(height):
        total += grid[row][col]

#print(total)
