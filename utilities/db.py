import sqlite3
import time
from random import randint

class DbService:
    def __init__(self):
        self.service_conn = sqlite3.connect(r"services.sqlite")
        self.monitor_conn = sqlite3.connect(r"monitor.sqlite")

    def insert_into_services(self,id,name,url,downtime):
        self.service_conn.execute("INSERT INTO SERVICES (ID,NAME,URL,DOWNTIME) VALUES (?,?,?,?)",(randint(0,99),name,url,downtime));
        self.service_conn.commit()

    def print_all(self):
        cursor = self.service_conn.execute("SELECT * from SERVICES")
        for row in cursor:
	        print "ID = ", row[0]
	        print "NAME = ", row[1]
	        print "url = ", row[2]

    def print_all_in_monitor(self):
        cursor = self.monitor_conn.execute("SELECT * from MONITOR")
        for row in cursor:
            print "ID = ", row[0]
            print "NAME = ", row[1]
            print "url = ", row[2]
            print "REASONFORFAILURE = ", row[3]
            print "DOWNTIME = ", row[4]

    def get_all_services_and_url(self):
        cursor = self.service_conn.execute("SELECT * from SERVICES")
        return cursor

    def insert_into_monitor(self,name,url,reason_for_failure):
        self.monitor_conn.execute("INSERT INTO MONITOR (ID,SERVICENAME,URL,REASONFORFAILURE) VALUES (?,?,?,?)",(randint(0,99),name,url,reason_for_failure));
        self.monitor_conn.commit()
