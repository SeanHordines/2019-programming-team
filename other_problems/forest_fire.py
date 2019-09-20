sequence = [1, 1]
N = int(input())
for n in range(2, N):
    temp = 0
    valid = False
    while(not valid):
        temp +=1
        valid = True
        max = (n-1)//2 + 1
        if(max == 1):
            max = 2
        for k in range(1, max):
            j = n - 2*k
            print("n:", n, "j:", j, "k:", k, "temp:", temp)
            dif1 = sequence[j] - sequence[j+k]
            dif2 = sequence[j+k] - temp
            if(dif1 == dif2):
                valid = False
                break
        
    sequence.append(temp)
print(sequence)
