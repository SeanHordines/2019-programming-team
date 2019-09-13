#simulate a loop falling down a braided rope

def shorten(string):
    len1 = len(string)
    len2 = 0
    while(len1 > len2):
        len1 = len(string)
        string = string.replace("XU", "")
        string = string.replace("UX", "")
        string = string.replace("YV", "")
        string = string.replace("VY", "")
        string = string.replace("ZW", "")
        string = string.replace("WZ", "")
        string = string.replace("AA\'", "")
        string = string.replace("A\'A", "")
        string = string.replace("BB\'", "")
        string = string.replace("B\'B", "")
        len2 = len(string)
    return string

def close(loop):
    len1 = len(loop)
    len2 = 0
    while(len1 > len2):
        len1 = len(loop)
        if((loop[0] == "U") and (loop[-1] == "X")):
            loop = loop[1:-1]
        elif((loop[0] == "V") and (loop[-1] == "Y")):
            loop = loop[1:-1]
        elif((loop[0] == "W") and (loop[-1] == "Y")):
            loop = loop[1:-1]
        len2 = len(loop)
    return loop

def drop(loop, braid):
    for cross in braid:
        temp = ""
        if(cross == "A"):
            for l in loop:
                if(l == "X"):
                    temp += "UYX"
                elif(l == "Y"):
                    temp += "X"
                elif(l == "Z"):
                    temp += "Z"
                elif(l == "U"):
                    temp += "UVX"
                elif(l == "V"):
                    temp += "U"
                elif(l == "W"):
                    temp += "W"
        elif(cross == "B"):
            for l in loop:
                if(l == "X"):
                    temp += "X"
                elif(l == "Y"):
                    temp += "VZY"
                elif(l == "Z"):
                    temp += "Y"
                elif(l == "U"):
                    temp += "U"
                elif(l == "V"):
                    temp += "WVZ"
                elif(l == "W"):
                    temp += "V"
        elif(cross == "C"):
            for l in loop:
                if(l == "X"):
                    temp += "Y"
                elif(l == "Y"):
                    temp += "YXV"
                elif(l == "Z"):
                    temp += "Z"
                elif(l == "U"):
                    temp += "V"
                elif(l == "V"):
                    temp += "YUV"
                elif(l == "W"):
                    temp += "W"
        elif(cross == "D"):
            for l in loop:
                if(l == "X"):
                    temp += "X"
                elif(l == "Y"):
                    temp += "Z"
                elif(l == "Z"):
                    temp += "ZYW"
                elif(l == "U"):
                    temp += "U"
                elif(l == "V"):
                    temp += "W"
                elif(l == "W"):
                    temp += "ZVW"

        temp = close(shorten(temp))
        loop = temp
    return loop

#contains X, Y, Z, X', Y', Z'
loop = input()

#X = loop clockwise around first  rope
#X'= loop anticlockwise around first rope => U
loop = loop.replace("X\'", "U")
#Y = loop clockwise around second rope
#Y'= loop anticlockwise around second rope => V
loop = loop.replace("Y\'", "V")
#Z = loop clockwise around third rope
#Z'= loop anticlockwise around third rope => W
loop = loop.replace("Z\'", "W")

#contains A, B, A', B'
braid = input()
#A = first rope crosses second
#A' = second rope crosses first => C
braid = braid.replace("A\'", "C")
#B = second rope crosses third
#B' = third rope crosses second => D
braid = braid.replace("B\'", "D")

loop = drop(close(shorten(loop)), shorten(braid))
loop = loop.replace("U", "X\'")
loop = loop.replace("V", "Y\'")
loop = loop.replace("W", "Z\'")
print(loop)
