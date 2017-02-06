import defensive_ranking
import csv

frontCourtPlayersAndRankings = {}
frontCourtPlayers = []

frontcourtfile = open("frontcourtplayers.txt")

for line in frontcourtfile:
    linelist = line.split()
    name = linelist[0] + " " + linelist[1]
    frontCourtPlayers.append(name)

for player in frontCourtPlayers:
    frontCourtPlayersAndRankings[player] = defensive_ranking.frontCourtRating()

frontcourtfile.close()

