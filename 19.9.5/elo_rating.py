n = int(input())
teams = []
elos = []
for i in range(n):
    line = input().split()
    team_name = line[0]
    teams.append(team_name)
    wlr = line[1]
    wins, losses = map(int, wlr.split("-"))
    rs = sum(map(int, line[2:]))
    elo = (rs + 400*(wins-losses))/(len(line)-2)
    elos.append(elo)


for i in range(len(teams)):
    index = -1
    for elo in elos:
        if (elo == max(elos)):
            index = elos.index(elo)
            break
    print(str(i+1) + ") " + teams[index] + " " + str(round(elos[index], 2)))
    elos[index] = -1
