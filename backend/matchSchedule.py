import random
import datetime


def matchScheduler(tournament_id,startMatchId,startDate,time,venues,teams):

    print("Teams : ",teams)
    print("Venues : ",venues.values)

    startDate = datetime.datetime.strptime(startDate,"%d-%m-%Y")    
    # print(startDate)

    schedule = {}
    n = len(teams)//2
    m = len(teams)-1

    pairs = []

    random.seed(random.choice([1,2,3,4]))

    for i in range(m):
        leg1 = []
        leg2 = []
        matchDone = set()
        for j in range(len(teams)//2):
            while(len(matchDone)!=8):
                twoTeams = random.sample(teams,2)
                if((twoTeams[0] not in matchDone) and (twoTeams[1] not in matchDone) and (twoTeams not in pairs)):
                    matchDone.add(twoTeams[0])
                    matchDone.add(twoTeams[1])
                    pairs.append(twoTeams)
                    # print()
                    leg1.append((tournament_id,startMatchId,startDate.strftime("%Y")+"-"+startDate.strftime("%m")+"-"+startDate.strftime("%d"),time,venues[twoTeams[0]],twoTeams[0],twoTeams[1]))
                    nextDate = startDate+datetime.timedelta(days=(m*n))
                    # print("Next rev match ", nextDate)
                    leg2.append((tournament_id,startMatchId+28,nextDate.strftime("%Y")+"-"+nextDate.strftime("%m")+"-"+nextDate.strftime("%d"),time,venues[twoTeams[1]],twoTeams[1],twoTeams[0]))
                    startMatchId+=1
                    startDate += datetime.timedelta(days=1)
                    
        schedule[i+1] = leg1
        schedule[i+len(teams)] = leg2

    tt = []
    for i in range(1,(m*2)+1):
        leg = schedule[i]
        for l in leg:
            print(l)

    return tuple(tt)


# teams = ["Mi","Rcb","Csk","Rr","Kkr","Srh","Pkbs","Dc"]
# venues = {
#           "Mi":"Wankhede Stadium",
#           "Rcb":"Chinaswammy Stadium",
#           "Csk":"MAC Stadium",
#           "Rr":"SMS Stadium",
#           "Kkr":"Eden Gardens",
#           "Srh":"RGI Stadium",
#           "Pkbs":"PCA Stadium",
#           "Dc":"AJ Stadium"
#          }

# matches = matchScheduler(1,1,"21-05-2021","16:00:00",venues,teams)


