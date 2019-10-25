from math import gcd

a, b, c, d = map(int, input().split())

coprimes = 0
for x in range(a, b+1):
    for y in range(c, d+1):
        if gcd(x, y) == 1:
            coprimes += 1

print(coprimes)
