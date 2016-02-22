import sqlite3
import sys
from create_ui import build_ui
from monitor.app import StartMonitoring

monitor = StartMonitoring()

run = {
    'setup': lambda: start_setup(),
    'monitor': lambda: start_monitoring()
}

def start_monitoring():
    conn = sqlite3.connect(r"monitor.sqlite")
    conn.execute('''CREATE TABLE if not exists MONITOR
           (ID INT PRIMARY KEY     NOT NULL,
           SERVICENAME           TEXT    NOT NULL,
           URL            TEXT     NOT NULL,
           REASONFORFAILURE            TEXT     NOT NULL,
           Timestamp DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')));''')
    monitor.run()

def start_setup():
    conn = sqlite3.connect(r"services.sqlite")
    conn.execute('''CREATE TABLE if not exists SERVICES
	       (ID INT PRIMARY KEY     NOT NULL,
	       NAME           TEXT    NOT NULL,
	       URL            INT     NOT NULL;''')
    build_ui()

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ['setup', 'monitor']:
        print("Usage python main.py [setup|monitor]")
        sys.exit(1)

    run[sys.argv[1]]()



