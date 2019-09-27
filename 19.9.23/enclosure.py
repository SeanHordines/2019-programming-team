from math import atan2, pi, pow, sqrt, hypot

n, k = map(int, input().split())

trees = []
for i in range(n):
    x, y = map(int, input().split())
    tree = [x, y]
    trees.append(tree)

def sort(sub_list):
    sub_list.sort(key = lambda x: x[2])
    return sub_list

avgx = 0
avgy = 0
myTrees = trees[:k]
for tree in myTrees:
    avgx += tree[0]/n
    avgy += tree[1]/n

print(avgx, avgy)

for tree in myTrees:
    tree.append(atan2(x-avgx, y-avgy)+pi)

myTrees = sort(trees[:k])
print(myTrees)

area = 0.0
for j in range(k-1):
    a = hypot(myTrees[j][0] - avgx, myTrees[j][1] - avgy)
    b = hypot(myTrees[j+1][0] - avgx, myTrees[j+1][1] - avgy)
    c = sqrt(pow(myTrees[j][0] - myTrees[j+1][0], 2) + pow(myTrees[j][1] - myTrees[j+1][1], 2))
    p = (a + b +c)/2
    area += sqrt(p*(p-a)*(p-b)*(p-c))

print(area)
