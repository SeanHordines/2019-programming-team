k = int(input())

you = input()
friend = input()

difs = 0
for n in range(len(you)):
    if you[n] != friend[n]:
        difs += 1

print(min(difs, len(you) - k) + min(len(you)-difs, k))
