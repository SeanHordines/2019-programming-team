from itertools import permutations

solved = {}
primes = {}

def nextPrime(p):
    if p in primes:
        return primes[p]
    else:
        temp = p
        valid = False
        while(not valid):
            temp += 1
            valid = True
            for i in range(1, p+1):
                if(temp%i==0):
                    valid = False
        primes[p] = temp
        print(temp)
        return temp


def uniquePerms(k):
    if k in solved:
        return solved[k]
    else:
        perms = set([])
        factors = []
        p = 2
        while(k != 1):
            p = nextPrime(p)
            while(k%p == 0):
                factors.append(p)
                k = k/p

        print(factors)
        temp = permutations(factors)
        for e in temp:
            perms.add(e)

        if(len(perms) == 0):
            perms.add(1)

        solved[k] = len(perms)
        return len(perms)




temp = input()
while(temp != ""):
    n = int(temp)
    k = 2
    while(uniquePerms(k) != n):
        k += 1
    print(n, k)
    temp = input()
