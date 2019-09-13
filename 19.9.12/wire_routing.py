n = input()
while(n):
    n = int(n)
    start = [int(x) for x in input().split()]
    end = [int(x) for x in input().split()]

    grid = []
    for y in range(n):
        grid.append(input().replace(" ", ""))

    def path(s, e):
        queue = []
        path = [s]
        queue.append(path)
        found = False
        while(not found):
            print(queue)
            path = queue.pop()
            node = path[-1]
            if node == end:
                found == True
                return path
                break

            if(node[0]-1 >= 0):
                if(grid[node[1]][node[0]-1] == "0"):
                    new = [node[0]-1, node[1]]
                    if(new not in path):
                        queue.append(path + [new])
            if(node[0]+1 < n):
                if(grid[node[1]][node[0]+1] == "0"):
                    new = [node[0]-1, node[1]]
                    if(new not in path):
                        queue.append(path + [new])
            if(node[1]-1 >= 0):
                if(grid[node[1]-1][node[0]] == "0"):
                    new = [node[0], node[1]-1]
                    if(new not in path):
                        queue.append(path + [new])
            if(node[1]+1 < n):
                if(grid[node[1]+1][node[0]] == "0"):
                    new = [node[0], node[1]+1]
                    if(new not in path):
                        queue.append(path + [new])



    print(len(path(start, end)))
    n = input()
