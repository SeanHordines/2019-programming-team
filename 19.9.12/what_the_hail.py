h = input()
s = h
while(h != ""):
    h= int(h)
    i = 0
    while(h != 4):
        i+=1
        if(h%2==0):
            h = h/2
        else:
            h = 3*h + 1
    print(i, "steps were necessary for", s)
    h = input()
    s = h
