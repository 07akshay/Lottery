import sqlite3


def checkUser(userID, contest_name):
    with sqlite3.connect("test.db") as con:  
        cur = con.cursor()
        qr = f"select * from token_tb where userID='{userID}' and contest='{contest_name}'"
        cur.execute(qr)
        con.commit()
        rows = cur.fetchall()
        if len(rows)!=0:
            return False
        else:
            return True


def tokenAvailable(token):
    with sqlite3.connect("test.db") as con:  
        cur = con.cursor()
        qr = f"select * from token_tb where token_number='{token.Number}'"
        cur.execute(qr)
        con.commit()
        rows = cur.fetchall()
        if len(rows)!=0:
            return False
        else:
            return True

        
def insertToDB(token):
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"insert into token_tb values('{token.User}','{token.Number}','{token.Contest}')"
        cur.execute(qr)
        con.commit()


def getContests():
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        qr = f"select * from contest_tb order by deadline DESC"
        cur.execute(qr)
        con.commit()
        rows = cur.fetchall()
        contests = []
        for row in rows:
            contests.append(row)
        return contests


def getWin():
    with sqlite3.connect("test.db") as con:  
        cur = con.cursor()
        qr = "select * from winners_tb order by deadline DESC"
        cur.execute(qr)
        con.commit()
        rows = cur.fetchall()
        winners = []
        for row in rows:
            winners.append(row)
    return winners