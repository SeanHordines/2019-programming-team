n = int(input()) + 1

def findPaths(n):
    total = 0
    paths = [[0]]
    while(len(paths) > 0):
        curr = paths.pop()
        index = curr[-1]
        for i in range(index+1, n):
            paths.append(curr + [i])
        #print(curr + [n])
        prob = 1
        for j in range(len(curr)):
            dif = n - curr[j]
            prob *= 1/dif
        total += prob*len(curr)

    print(total)

findPaths(n)
