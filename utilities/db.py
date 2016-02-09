import sqlite3
from random import randint

class DbService:
    def __init__(self):
        self.conn = sqlite3.connect(r"services.sqlite")

    def insert(self,id,name,url,downtime):
        self.conn.execute("INSERT INTO SERVICES (ID,NAME,URL,DOWNTIME) VALUES (?,?,?,?)",(randint(0,99),name,url,downtime));

    def print_all(self):
        cursor = self.conn.execute("SELECT *  from SERVICES")
        for row in cursor:
	        print "ID = ", row[0]
	        print "NAME = ", row[1]
	        print "url = ", row[2]
	        print "downtime = ", row[3]
