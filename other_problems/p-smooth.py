for t in range(int(input())):
    p, n = map(int, input().split())

    numbers = [1]
    i, j, k = 0, 0, 0
    two, three, five = 2*numbers[i], 3*numbers[j], 5*numbers[k]
    while(len(numbers) < n):
        if min(two, three, five) == two:
            if(two not in numbers):
                numbers.append(two)
            i+=1
            two = 2*numbers[i]
        elif min(two, three, five) == three:
            if(three not in numbers):
                numbers.append(three)
            j+=1
            three = 3*numbers[j]
        elif min(two, three, five) == five:
            if(five not in numbers):
                numbers.append(five)
            k+=1
            five = 5*numbers[k]
        else:
            print("fail")
        #print(numbers)
        #print(numbers[-1])


    print("" + str(n) + "th term of " + str(p) + "-smooth series is: " + str(numbers[-1]))
