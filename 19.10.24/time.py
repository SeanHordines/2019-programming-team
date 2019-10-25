n, s = map(int, input().split())
time = max([float(x)/1000 for x in input().split()])
time = s*time
time = round(time + 0.5)
print(time)
