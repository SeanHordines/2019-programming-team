from itertools import combinations
from math import factorial

line = input()
chars = ""
for c in line:
    if not (c in chars):
        chars += c

def nCr(a, b):
    return (factorial(a)/(factorial(b)*factorial(a-b)))

def total(list):
    if(len(list) > 2):
        return nCr(line.count(list[0]), total(list[1:]))
    else:
        return nCr(line.count(list[0]), line.count(list[1]))

sum = 0
for i in range(len(chars) + 1):
    combs = combinations(chars, i)
    for comb in combs:
        sum += total(comb)

print(sum % 11092019)
