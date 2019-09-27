import string

s = input()
delta = 0
index = 0
for i in range(26):
    index = s.find(string.ascii_lowercase[i])
    if index == -1:
        delta += 1
    else:
        s = s[index+1:]

print(delta)
