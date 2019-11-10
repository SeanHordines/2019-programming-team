alpha = input()
line = input()
words = []

for i in range(len(line)):
    words.append(line[0:i] + line[i+1:])

    for j in range(len(alpha)):
        words.append(line[:i] + alpha[j] + line[i:])
        words.append(line[:i] + alpha[j] + line[i+1:])

for j in range(len(alpha)):
    words.append(line + alpha[j])

words.sort()
print(" ")

while(len(words) > 0):
    if(words[0] == line):
        pass
    elif(words.count(words[0]) == 1):
        print(words[0])
    words.remove(words[0])
