import defensive_ranking
import pandas

frontCourtPlayersAndRankings = {}
frontCourtPlayers = []

frontcourtfile = open("frontcourtplayers.txt")

for line in frontcourtfile:
    linelist = line.split()
    name = linelist[0] + " " + linelist[1]
    frontCourtPlayers.append(name)

#for player in frontCourtPlayers:
    #frontCourtPlayersAndRankings[player] = defensive_ranking.frontCourtRating(defensive_ranking.getIDWithName(player))

frontcourtfile.close()

#print(frontCourtPlayersAndRankings)
#print(frontCourtPlayers)
print(defensive_ranking.frontCourtRating(defensive_ranking.getIDWithName("DeMarre Carroll")))

