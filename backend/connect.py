from database import Database
from matchSchedule import matchScheduler



def validateAdmin(id_,password):
    admin = Database.getData("admin",["admin_id",id_])
    if admin[0][1]==password:
        print("Authenticated")
        return 2
    return 0

def validateTeam(id_,password):
    team = Database.getData("team",["team_id",id_])
    if len(team)==0:
        return 1
    if team[0][1]==password:
        print("Authenticated")
        return 2
    return 0

def getTournaments():
    tournaments = Database.getData(table_name = "tournament")
    return tournaments

def getTeamNames ():
    teams = Database.getColumnsOf(table_name = "team",columns=["team_name"])
    teams = [t[0] for t in teams]
    return teams

def getTeamHomeGrounds():
    names = teamIDs()
    home_grounds = Database.getColumnsOf(table_name = "team", columns = ["home_ground"])
    home_grounds = [t[0] for t in home_grounds]    
    venues = dict(zip(names,home_grounds))
    return venues


def getTeamIDMapping():
    result = Database.getColumnsOf(table_name="team", columns = ["team_name","team_id"])
    mapping = {}
    for r in result:
        mapping[r[0]] = r[1]
    return mapping

def getTeamNameMapping():
    result = Database.getColumnsOf(table_name="team", columns = ["team_name","team_id"])
    mapping = {}
    for r in result:
        mapping[r[1]] = r[0]
    return mapping

def teamIDs():
    result = Database.getColumnsOf(table_name="team", columns = ["team_id"])
    result = [r[0] for r in result]
    return result

def getPlayerId(name):
    query = "SELECT p_id FROM player_info WHERE first_name = '{}'".format(name.split(" ")[0])
    result = Database.runQuery(query)[0]
    return result[0]

def getTeamPlayers(team_id):
    query = "SELECT player_info.p_id,first_name,last_name,player_type FROM player_info INNER JOIN  player ON player.p_id = player_info.p_id WHERE player.team_id = {}".format(team_id)
    result = Database.runQuery(query)
    result = [(x[0],x[1]+" "+x[2],x[3]) for x in result]
    return result
  

def addTournament(name,host,year,prize_money,startDate,adminId):

    new_tournamentId = Database.getRowCount("tournament","tournament_id") + 1
    new_matchId = Database.getRowCount("matches","m_id") + 1

    teams = teamIDs()
    venues = getTeamHomeGrounds()

    schedule = matchScheduler(new_tournamentId,new_matchId,startDate,"16:00:00.0",venues,teams)

    # print("LAST MATCH : ",schedule[-1])

    numberOfMatches = len(schedule)
    print("Number of matches : ",numberOfMatches)

    columns = """
            INSERT INTO tournament 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
    
    values = (new_tournamentId,name,host,year,numberOfMatches,prize_money,None,adminId)
    
    Database.insertQuery(columns,values)
    print("Tournament Created!")

    Database.insertMultipleRows("matches",schedule)
    print("Matches scheduled!")

    return True


def getMatchesForAdmin(tournament_id):
    matches = Database.getData("matches",["tournament_id",tournament_id+""])
    return matches

def getMatchesForTeam(team_id):
    query = "SELECT * from matches WHERE home_team = {t_id} OR away_team = {t_id}".format(t_id=team_id)
    matches = Database.runQuery(query)
    return matches

def getPointsTable(tournament_id):

    query = "SELECT * FROM points_table WHERE tournament_id = {} ORDER BY points DESC".format(tournament_id)
    points_table = Database.runQuery(query)
    # points_table = Database.getData("points_table",["tournament_id",tournamet_id+""])
    return points_table

def addMatchResult( m_id,toss_won,
                    overs1,runs1,wickets1,extras1,
                    overs2,run2,wickets2,extras2,
                    man_of_the_match,winning_team,losing_team):

    teamMap = getTeamIDMapping()
    toss_won = teamMap[toss_won]
    winning_team = teamMap[winning_team]
    losing_team = teamMap[losing_team]
    man_of_the_match = getPlayerId(man_of_the_match)

    query = """
            INSERT INTO match_summary
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
    values = (m_id,toss_won,overs1,runs1,wickets1,extras1,overs2,run2,wickets2,extras2,
                    man_of_the_match,winning_team,losing_team)

    Database.insertQuery(query,values)
    return True
    
def playersInMatch(match_id):

    query = "SELECT home_team,away_team FROM matches WHERE m_id = {}".format(match_id)
    result = Database.runQuery(query)[0]
    team1 = getTeamPlayers(result[0])
    team2 = getTeamPlayers(result[1])
    team1.extend(team2)
    players = [x[1] for x in team1]
    return players


def addPlayerToTeam(team_id,first_name,last_name,type_,email):
    p_id = Database.getRowCount("player","p_id") + 1
    print("ROW COUNT : ",p_id)
    query = """
            INSERT INTO player 
            VALUES (%s,%s,%s,%s,%s,%s)
            """
    values = (p_id,team_id,type_,0,0,0)
    Database.insertQuery(query,values)
    print("Inserted into Players Table")

    query2 = """
             INSERT INTO player_info
             VALUES (%s,%s,%s,%s,%s)
             """
    values = (p_id,first_name,last_name,first_name[:2]+"."+last_name+"@gmail.com",None)
    Database.insertQuery(query2,values)
    print("Inserted into PlayerInfo table!")
    return True

    
def matchResult(team_id):
    idToName = getTeamNameMapping()
    query = "SELECT * FROM match_summary_view WHERE home_team = '{}' OR away_team = '{}'".format(idToName[int(team_id)],idToName[int(team_id)])
    result = Database.runQuery(query)
    # result = Database.getData("match_summary_view")
    nameToId = getTeamIDMapping()
    refined = []
    for r in result:
        temp = [r[0]]
        temp.append(r[4].strftime("%d-%m-%Y"))
        if nameToId[r[1]] == team_id:
            temp.append(r[2])
        else:
            temp.append(r[1])
        temp.append(r[5])
        temp.append(r[13])
        temp.append(str(r[6])+"-"+str(r[8]))
        temp.append(str(r[9])+"-"+str(r[11]))
        temp.append(r[12])
        refined.append(temp)
    return refined





    




