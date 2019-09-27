cases = int(input())
for _ in range(cases):
    d = {}
    for _ in range(int(input())):
        n, c = input().split()
        if n in d.keys():
            d[n] += int(c)
        else:
            d[n] = int(c)

        l = []
        for k in d.keys():
            l.append((k,d[k]))

    l.sort(key=lambda x: x[0])
    l.sort(key=lambda x: x[1],reverse = True)

    print(len(l))
    [print(i[0] + " " + str(i[1])) for i in l]
