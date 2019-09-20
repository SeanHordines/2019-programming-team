n = input()
per = 0
while(len(n) > 1):
    per += 1
    prod = 1
    for c in n:
        prod *= int(c)
    n = str(prod)
print(per)
