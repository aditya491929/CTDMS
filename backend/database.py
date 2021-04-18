import psycopg2


class Database:

    con = None

    @staticmethod
    def openConnection():
        Database.con = psycopg2.connect(database="CTDMS",user="postgres",password="aditya491@",host="127.0.0.1",port="5432")
        print("Database connected successfully!")

    @staticmethod
    def closeConnection():
        Database.con.close()
        print("Connection closed successfully!")

    @staticmethod
    def getCursor():
        if(Database.con):
            return Database.con.cursor()
        else:
            print("Open Connection First")
            return False

    @staticmethod
    def commitConnection():
        Database.con.commit()

    @staticmethod
    def getData(table_name,filter_by=None):
        Database.openConnection()
        cur = Database.getCursor()
        if(filter_by):
            cur.execute("SELECT * from {} WHERE {} = {}".format(table_name,filter_by[0],filter_by[1]))
        else:
            cur.execute("SELECT * from {}".format(table_name))
        result = cur.fetchall()
        print("Results fetched successfully!")
        Database.closeConnection()
        return result

    @staticmethod
    def runQuery(query):
        Database.openConnection()
        cur = Database.getCursor()
        cur.execute(query)
        results = cur.fetchall()
        print("Query returned successfully")
        Database.closeConnection()
        return results

    @staticmethod
    def insertQuery(query,values):
        Database.openConnection()
        cur = Database.getCursor()
        try:
            cur.execute(query,values)
            Database.commitConnection()
            count = cur.rowcount
            print("{} records inserted!".format(count))
        except (psycopg2.Error) as e:
            print(e)
        finally:
            Database.closeConnection()

    @staticmethod
    def getRowCount(table_name):
        Database.openConnection()
        cur = Database.getCursor()
        try:
            cur.execute("SELECT MAX(p_id) FROM {}".format(table_name))
            result = cur.fetchone()
            print("Query returned successfully!")
            return result[0]
        except (psycopg2.Error) as e:
            print(e)
        finally:
            Database.closeConnection()
    
    

    




# with open("./resources/teams.json","r") as read_file:
#     team_data = json.load(read_file)

# print(team_data['2'])