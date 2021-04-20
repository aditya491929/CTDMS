from database import Database
from matchSchedule import matchScheduler

def validateAdmin(id,password):
    admin = Database.getData("admin",["admin_id",id])
    if len(admin)==0:
        return 1
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
    return teams[:2]

def getTeamHomeGrounds():
    names = getTeamNames()
    home_grounds = Database.getColumnsOf(table_name = "team", columns = ["home_ground"])
    venues = dict(zip(names,home_grounds))
    return venues

def getTeamPlayers(team_id):
    query = "SELECT player_info.p_id,first_name,last_name,player_type FROM player_info INNER JOIN  player ON player.p_id = player_info.p_id WHERE player.team_id = {}".format(team_id)
    result = Database.runQuery(query)
    result = [(x[0],x[1]+" "+x[2],x[3]) for x in result]
    return result
  

def addTournament(name,host,year,prize_money,startDate,adminId):

    new_tournamentId = Database.getRowCount("tournament","tournament_id") + 1
    new_matchId = Database.getRowCount("matches","m_id") + 1

    teams = getTeamNames()
    venues = getTeamHomeGrounds()

    schedule = matchScheduler(new_tournamentId,new_matchId,startDate,"16:00:00.0",venues,teams)

    print("LAST MATCH : ",schedule[-1])

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
    points_table = Database.getData("points_table",["tournament_id",tournament_id+""])
    return points_table

def addMatchResult( m_id,toss_won,
                    overs1,runs1,wickets1,extras1,
                    overs2,run2,wickets2,extras2,
                    man_of_the_match,winning_team,losing_team):
    query = """"
            INSERT INTO match_summary
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
    values = (m_id,toss_won,overs1,runs1,wickets1,extras1,overs2,run2,wickets2,extras2,
                    man_of_the_match,winning_team,losing_team)

    Database.insertQuery(query,values)
    return True
    

def addPlayerToTeam(team_id,first_name,last_name,type_,email):
    p_id = Database.getRowCount("player","p_id") + 1
    print("ROW COUNT : ",p_id)
    
    query = """
            INSERT INTO player 
            VALUES (%s,%s,%s,%s,%s,%s)
            """
    values = (p_id,team_id,type_,0,0,0)
    Database.insertQuery(query,values)
    
    query2 = """
             INSERT INTO player_info
             VALUES (%s,%s,%s,%s,%s)
             """
    values = (p_id,first_name,last_name,email,None)
    Database.insertQuery(query2,values)
    return True

    




    




