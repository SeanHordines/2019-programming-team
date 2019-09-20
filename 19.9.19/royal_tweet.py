total = 0

for i in range(int(input())):
    line = input().lower()
    if(line.count("@britishmonarchy") > 0):
        total += 1

print("Total Tweets Containing @BritishMonarchy =", total)
