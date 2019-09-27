import math

n, a, b = map(int, input().split())

def tenToBase(number, base):
    newNum = ""
    i = 1
    while(number > 0):
        newNum = str(number%base) + newNum
        number = number//math.pow(base, i)
        i += 1
    return newNum

while(True):
    alpha = tenToBase(n, a)
    beta = tenToBase(n, b)
    asum = sum(int(c) for c in alpha)
    bsum = sum(int(c) for c in beta)
    if asum == bsum:
        print(n, alpha, beta)
        break
    else:
        n += 1
