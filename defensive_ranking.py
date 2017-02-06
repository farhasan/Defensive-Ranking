import requests

traditionalStatURL = "http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
onoffRbURL1 = "http://stats.nba.com/stats/teamplayeronoffdetails?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&TeamID="
onoffRbURL2 = "&VsConference=&VsDivision="
onoffTOURL1 = "http://stats.nba.com/stats/teamplayeronoffdetails?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Opponent&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&TeamID="
onoffTOURL2 = "&VsConference=&VsDivision="
defURL = "http://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Defense&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
hustleURL = "http://stats.nba.com/stats/leaguehustlestatsplayer?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
shotURL = "http://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=&DistanceRange=5ft+Range&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Opponent&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
teamStatsScoringURL = "http://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Scoring&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision="

u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

traditionalResponse = requests.get(traditionalStatURL, headers = {"USER_AGENT": u_a})
traditionalResponse.raise_for_status()
traditionalStats = traditionalResponse.json()

playerTraditionalStats = traditionalStats['resultSets'][0]['rowSet']

playerDict = {}

for player in playerTraditionalStats:
    playerDict[player[0]] = player[1]

#remember there is a frontcourt formula and a backcourt formula

def getIDWithName(name):#get player id with name
    for player in playerTraditionalStats:
        


def accessStatsWithID(ID): #get full list of stats for player
    for player in playerTraditionalStats:
        if (ID == player[0]):
            return player

def getTeam(playerStats): #get the team id of player given stats
    team = playerStats[2]
    return team

def getOnCourtRebounding(ID): #get player's team's defensive rebounding percentage while player is on the floor
    playerStats = accessStatsWithID(ID)
    team = getTeam(playerStats)
    fullOnOffRbUrl = onoffRbURL1 + str(team) + onoffRbURL2
    onoffRbResponse = requests.get(fullOnOffRbUrl, headers={"USER-AGENT": u_a})
    onoffRbResponse.raise_for_status()
    onoffStats = onoffRbResponse.json()['resultSets'][1]['rowSet']
    onCrtRb = 0
    for player in onoffStats:
        if(player[4] == ID):
            onCrtRb = player[22]
    return onCrtRb

def getReboundingPct(ID): #gets players drb pct
    defURLResponse = requests.get(defURL, headers={"USER-AGENT": u_a})
    defURLResponse.raise_for_status()
    defStats = defURLResponse.json()['resultSets'][0]['rowSet']
    drbPCT = 0
    for player in defStats:
        if (player[0] == ID):
            drbPCT = player[12]
    return drbPCT

def getOnCourtOppFG(ID): #oppoosing team fg while player on court
    playerStats = accessStatsWithID(ID)
    team = getTeam(playerStats)
    fullOnOffTOUrl = onoffTOURL1 + str(team) + onoffTOURL2
    onoffFGResponse = requests.get(fullOnOffTOUrl, headers={"USER-AGENT": u_a})
    onoffFGResponse.raise_for_status()
    onoffStats = onoffFGResponse.json()['resultSets'][1]["rowSet"]
    for player in onoffStats:
        if (player[4] == ID):
            onCrtOppFG = player[14]
    return onCrtOppFG

def getPF(ID): #gets fouls per game
    gameStats = accessStatsWithID(ID)
    PF = gameStats[27]
    return PF

def getBlocks(ID): #gets blocks per game
    gameStats = accessStatsWithID(ID)
    blocks = gameStats[25]
    return blocks

def getBlocksAttempted(ID): #gets blocks attempted per game
    gameStats = accessStatsWithID(ID)
    blocksA = gameStats[26]
    return blocksA

def getBlockPCT(ID): #gets block percentage (percentage of opposing teams possessions that result in blocks)
    defURLResponse = requests.get(defURL, headers={"USER-AGENT": u_a})
    defURLResponse.raise_for_status()
    defStats = defURLResponse.json()['resultSets'][0]['rowSet']
    blockPCT = 0
    for player in defStats:
        if(player[0] == ID):
            blockPCT = player[17]
    return blockPCT

def getSteals(ID): #gets steals per game
    gameStats = accessStatsWithID(ID)
    steals = gameStats[24]
    return steals

def getStealPCT(ID): #gets percentage of opposing teams possesions that turn to steals
    defURLResponse = requests.get(defURL, headers={"USER-AGENT": u_a})
    defURLResponse.raise_for_status()
    defStats = defURLResponse.json()['resultSets'][0]['rowSet']
    for player in defStats:
        if(player[0] == ID):
            stealPCT = player[15]
    return stealPCT

#what percentage of attempted steals and blocks are fouls?
#how many fouls do the best defenders average?

def getMinutesPerGame(ID): #minutes per game
    gameStats = accessStatsWithID(ID)
    minutes = gameStats[9]
    return minutes

def getFoulsPerMinute(ID): #fouls per minute of play
    minutes = getMinutesPerGame(ID)
    fouls = getPF(ID)
    PFM = fouls / minutes
    return PFM

def getOppPaintPoints(ID): #opponents points in the paint while player is on the floor
    defURLResponse = requests.get(defURL, headers={"USER-AGENT": u_a})
    defURLResponse.raise_for_status()
    defStats = defURLResponse.json()['resultSets'][0]['rowSet']
    paintPoints = 0
    for player in defStats:
        if(player[0] == ID):
            paintPoints = player[21]
    return paintPoints

def getPointsinPaint(teamID):
    teamResponse = requests.get(teamStatsScoringURL, headers={"USER-AGENT": u_a})
    teamResponse.raise_for_status()
    teamStats = teamResponse.json()['resultSets'][0]['rowSet']
    pointsInThePaint = 0
    for team in teamStats:
        if(team[0] == teamID):
            pointsInThePaint= team[26]
    return pointsInThePaint

def getPCTTeamPainPoints(teamID, ID): #what percent of the teams paint points come when that player is playing?
    teamResponse = requests.get(teamStatsScoringURL, headers={"USER-AGENT": u_a})
    defURLResponse = requests.get(defURL, headers={"USER-AGENT": u_a})

    teamResponse.raise_for_status()
    defURLResponse.raise_for_status()

    teamStats = teamResponse.json()['resultSets'][0]['rowSet']
    defStats = defURLResponse.json()['resultSets'][0]['rowSet']

    pointsInThePaint = 0
    paintPoints = 0

    for team in teamStats:
        if (team[0] == teamID):
            pointsInThePaint = team[26]

    for player in defStats:
        if (player[0] == ID):
            paintPoints = player[21]

    paintpct = paintPoints/pointsInThePaint
    return paintpct


#difficult to use points in the paint because if you use opponents paint points while player on the floor
#you need to figure out what percentage of opposing team's points are paint points on average
#but if a player spends a lot of minutes on the floor it makes sense that those points are scored while
#player is on the floor, so paint points is not a great stat to use

def getDeflections(ID): #deflections per game
    hustleResponse = requests.get(hustleURL, headers={"USER-AGENT": u_a})
    hustleResponse.raise_for_status()
    hustleStats = hustleResponse.json()['resultSets'][0]['rowSet']
    for player in hustleStats:
        if (player[0] == ID):
            deflections = player[10]
    return deflections

def getCharges(ID): #charges per game
    hustleResponse = requests.get(hustleURL, headers={"USER-AGENT": u_a})
    hustleResponse.raise_for_status()
    hustleStats = hustleResponse.json()['resultSets'][0]['rowSet']
    for player in hustleStats:
        if (player[0] == ID):
            charges = player[9]
    return charges

def getContests(ID): #shots contested per game
    hustleResponse = requests.get(hustleURL, headers={"USER-AGENT": u_a})
    hustleResponse.raise_for_status()
    hustleStats = hustleResponse.json()['resultSets'][0]['rowSet']
    for player in hustleStats:
        if (player[0] == ID):
            contestedShots = player[6]
    return contestedShots

def contestedShotsPM(ID): #shots contested per minute
    hustleResponse = requests.get(hustleURL, headers={"USER-AGENT": u_a})
    hustleResponse.raise_for_status()
    hustleStats = hustleResponse.json()['resultSets'][0]['rowSet']
    for player in hustleStats:
        if (player[0] == ID):
            contestedShots = player[6]
            minutes = getMinutesPerGame(ID)
    contestsPM = contestedShots/minutes
    return contestsPM

def getFG5(ID): #field goal percentage less than five feet away
    opShotResponse = requests.get(shotURL, headers={"USER-AGENT": u_a})
    opShotResponse.raise_for_status()
    opShot5Stats = opShotResponse.json()['resultSets']['rowSet']
    FiveFG = 0
    for player in opShot5Stats:
        if (player[0] == ID):
            FiveFG = player[7]
    return FiveFG

def getFG59(ID): #fg pct 5-9 ft away
    opShotResponse = requests.get(shotURL, headers={"USER-AGENT": u_a})
    opShotResponse.raise_for_status()
    opShot59Stats = opShotResponse.json()['resultSets']['rowSet']
    Five9FG = 0
    for player in opShot59Stats:
        if (player[0] == ID):
            Five9FG = player[10]
    return Five9FG

def getFG1014(ID): #fg pct 10-14 away
    opShotResponse = requests.get(shotURL, headers={"USER-AGENT": u_a})
    opShotResponse.raise_for_status()
    opShot1014Stats = opShotResponse.json()['resultSets']['rowSet']
    Ten14FG = 0
    for player in opShot1014Stats:
        if (player[0] == ID):
            Ten14FG = player[13]
    return Ten14FG

def getFG1519(ID): #fg pct 15-19 away
    opShotResponse = requests.get(shotURL, headers={"USER-AGENT": u_a})
    opShotResponse.raise_for_status()
    opShot1519Stats = opShotResponse.json()['resultSets']['rowSet']
    Fifteen19FG = 0
    for player in opShot1519Stats:
        if (player[0] == ID):
            Fifteen19FG = player[16]
    return Fifteen19FG

def getFG2024(ID): #fg pct 20-24 away, three point territory
    opShotResponse = requests.get(shotURL, headers={"USER-AGENT": u_a})
    opShotResponse.raise_for_status()
    opShot2024Stats = opShotResponse.json()['resultSets']['rowSet']
    Twen24FG = 0
    for player in opShot2024Stats:
        if (player[0] == ID):
            Twen24FG = player[16]
    return Twen24FG

def getFG2529(ID): #fg pct 25-29 away
    opShotResponse = requests.get(shotURL, headers={"USER-AGENT": u_a})
    opShotResponse.raise_for_status()
    opShot2529Stats = opShotResponse.json()['resultSets']['rowSet']
    Twen29FG = 0
    for player in opShot2529Stats:
        if (player[0] == ID):
            Twen29FG = player[19]
    return Twen29FG

def frontCourtRating(ID):
    charges = getCharges(ID) * (.5)
    contestedshots = getContests(ID)
    blkPct = getBlockPCT(ID)
    oppTeamFG = getOnCourtOppFG(ID)
    oppPaintPoints = getOppPaintPoints(ID) * (.75)
    pfPM = getFoulsPerMinute(ID) * (.75)
    teamDRB = getOnCourtRebounding(ID) * (.75)
    drb = getReboundingPct(ID)
    lessthan5 = getFG5(ID)
    fg59 = getFG59(ID)
    fg1014 = getFG1014(ID)

    #how do you determine what score is a good score? it is probably based on context so rank the players first,
    #see if the rankings resemble actually well ranked players, then go from there

    score = charges + contestedshots + blkPct + oppTeamFG + oppPaintPoints + pfPM + teamDRB + drb + lessthan5 + fg59 + fg1014

    return score

#def backCourtRating(ID):

#backcourt- use deflections(what percent of opponents possessions are deflected?)- * 1, contested shots (needs total amount of opposing shots to get a percentage) * 1, stl pctg * 1, opp to pctg * 1, opp fg * 1, personal foul/minute * .5,, opponent fg 10-14 * 1, opp fg 15-19 * 1, opp fg 20-24 *1
#frontcourt- use charges * .5, contested shots * 1, blk pctg * 1, opp team fg on court * 1, blks pctg * 1, pf/min * .75, drb% * 1, opp paint points *(.75) opp fg less than 5 * 1, opponent fg 5-9 *1, opp fg 10-14 *1

#frontCourtRating(201599)