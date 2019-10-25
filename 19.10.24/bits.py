from math import pow

k, b = map(int, input().split())

c = 0

for i in range(0, int(pow(2, b)-1) + 1, k):
    temp = bin(i)[2:]
    c += temp.count("1")

print(c % 1000000009)
