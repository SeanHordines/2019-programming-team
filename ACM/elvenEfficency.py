#binary bears d
#room 251

n, m = map(int, input().split())

stones = []
numbers = []

for i in range(n):
    stones.append(int(input()))

for i in range(m):
    numbers.append(int(input()))

count = 0
for i in range(m):
    for j in range(n):
        if(stones[j] % numbers[i] == 0):
            stones[j] += 1
            count += 1

print(count)
