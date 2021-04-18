from database import Database

def validateAdmin(id,password):
    admin = Database.getData("admin",["admin_id",id])
    if admin[0][1]==password:
        return True
    return False

def getTournaments():
    tournaments = Database.getData(table_name = "tournament")
    return tournaments

def addTournament():
    pass

def getMatchesForAdmin(tournament_id):
    matches = Database.getData("matches",["tournament_id",tournament_id+""])
    return matches

def getMatchesForTeam(team_id):
    query = "SELECT * from matches WHERE home_team = {t_id} OR away_team = {t_id}".format(t_id=team_id)
    matches = Database.runQuery(query)
    return matches

def getPointsTable(tournamet_id):
    points_table = Database.getData("points_table",["tournament_id",tournamet_id+""])
    return points_table

def addMatchResult( m_id,toss_won,
                    overs1,runs1,wickets1,extras1,
                    overs2,run2,wickets2,extras2,
                    man_of_the_match,winning_team,losing_team):
    query = """"
            INSERT INTO match_summary
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
    values = tuple(m_id,toss_won,overs1,runs1,wickets1,extras1,overs2,run2,wickets2,extras2,
                    man_of_the_match,winning_team,losing_team)

    Database.insertQuery(query,values)
    return True
    

def addPlayerToTeam(team_id,first_name,last_name,type_,email):
    p_id = Database.getRowCount("player") + 1
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
    




    




