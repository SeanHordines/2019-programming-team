from itertools import combinations

n, k = map(int, input().split())
difficulties = [int(x) for x in input().split()]

count = 0

contests = combinations(difficulties, k)
for c in contests:
    valid = True
    for e in c:
        if c.count(e) > 1:
            valid = False
            break
    if valid:
        count += 1

print(count % 998244353)            
