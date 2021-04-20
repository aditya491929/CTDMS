import psycopg2


class Database:

    con = None

    @staticmethod
    def openConnection():
        Database.con = psycopg2.connect(database="CTDMS",user="postgres",password="RAHUL@postgres",host="127.0.0.1",port="5432")
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
    def getColumnsOf(table_name,columns):
        Database.openConnection()
        cur = Database.getCursor()
        column_string = ",".join(columns)
        query = "SELECT {} FROM {}".format(column_string,table_name)
        print("QUERY : ", query)
        cur.execute(query)
        results = cur.fetchall()
        print("Query returned successfully")
        return results


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
            return True
        except (psycopg2.Error) as e:
            print(e)
            return False
        finally:
            Database.closeConnection()


    @staticmethod
    def insertMultipleRows(table,values):
        Database.openConnection()
        cur = Database.getCursor()
        help_str = "({})".format(','.join("%s" for x in range(len(values[0]))))
        print(help_str)
        args_str = ','.join(cur.mogrify(help_str,x).decode('utf-8') for x in values)
        query = "INSERT INTO "+table+" VALUES "+args_str

        try:
            cur.execute(query)
            Database.commitConnection()
            count = cur.rowcount
            print("{} records inserted!".format(count))
            return True
        except (psycopg2.Error) as e:
            print(e)
            return False
        finally:
            Database.closeConnection()
            


    @staticmethod
    def getRowCount(table_name,pk):
        Database.openConnection()
        cur = Database.getCursor()
        try:
            cur.execute("SELECT MAX({}) FROM {}".format(pk,table_name))
            result = cur.fetchone()
            print("Query returned successfully!")
            return result[0]
        except (psycopg2.Error) as e:
            print(e)
        finally:
            Database.closeConnection()
    