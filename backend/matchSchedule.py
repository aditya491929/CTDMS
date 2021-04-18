import random
import datetime

teams = ["Mi","Csk","Rcb","Srh","Kkr","Pkbs","Rr","Dc"]

def matchScheduler(teams,startDate):

    startDate = datetime.datetime(2021,5,19)

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
                revTwoTeams = twoTeams[::-1]
                if((twoTeams[0] not in matchDone) and (twoTeams[1] not in matchDone) and (twoTeams not in pairs)):
                    matchDone.add(twoTeams[0])
                    matchDone.add(twoTeams[1])
                    pairs.append(twoTeams)
                    # print()
                    startDate += datetime.timedelta(days=1)
                    leg1.append([twoTeams,startDate.strftime("%d")+"-"+startDate.strftime("%m")+"-"+startDate.strftime("%Y")])
                    nextDate = startDate+datetime.timedelta(days=(n-(j+1)+(m*n)))
                    # print("Next rev match ", nextDate)
                    leg2.append([revTwoTeams,nextDate.strftime("%d")+"-"+nextDate.strftime("%m")+"-"+nextDate.strftime("%Y")])
        schedule[i+1] = leg1
        schedule[i+len(teams)] = leg2

    tt = []
    for i in range(1,(m*2)+1):
        leg = schedule[i]
        for l in leg:
            tt.append([l[0][0],l[0][1],l[1]])
            print("{} VS {} | {}".format(l[0][0], l[0][1], l[1]))

    # print(tt[-1])
    return tt