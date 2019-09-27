def check(inp, c):
    for off in range(len(inp)+1):
        count = 0
        temp = c
        while True:
            if off+count < len(c) and inp[off+count] in c:
                temp = temp.replace(inp[off+count],"",1)
                count += 1
                if len(temp) == 0:
                    #print(True)
                    return off
            else:
                break
    #print(False)
    return False
for _ in range(int(input())):
    a = input()
    b = input()
    pos = -1
    length = 1
    for off in range(len(b)+1):
        #print(off)
        count = 1
        c = check(a, b[off:off+count])
        while c and off+count < len(b):
            #print(b[off:off+count])
            count += 1
            c = check(a, b[off:off+count])
        if count > length:
            pos = c
            length = count
    if pos >= 0:
        print(a[pos:pos+length])
    else:
        print("NONE")
