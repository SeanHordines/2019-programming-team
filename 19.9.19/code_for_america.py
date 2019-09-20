city = input()
while(city != "End"):
    if(city == ""):
        city = input()
        if(city == "End"):
            break

    temp = input()
    while(temp == ""):
        temp = input()
    text = temp
    temp = input()
    while(temp != ""):
        text = text + temp
        temp = input()

    text = text.lower()
    if((text.count("lead") > 0) and (text.count("flexib") > 0) and (text.count("involve") > 0) and (text.count("plan") > 0)):
        print(city + ": Meets standards")
    else:
        print(city + ": Does not meet standards")

    city = input()
