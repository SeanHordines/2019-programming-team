line = input().replace(" ", "")
operators = ["+", "-", "*", "/"]
while(line != ""):
    ops = []
    exps = []
    for i in range(len(line)):
        if line[i] in operators:
            ops.append(line[i])
        else:
            exps.append(line[i])
            while(len(exps) > 1):
                a = exps.pop()
                b = exps.pop()
                temp = "(" + b + " " + ops.pop() + " " + a + ")"
                exps.append(temp)
    print(exps[0])

    line = input().replace(" ", "")
