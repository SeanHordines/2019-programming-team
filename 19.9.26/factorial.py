for _ in range(int(input())):
    a = int(input())
    s = 1
    for i in range(a):
        s *= i+1
    print(s%10)
