import sqlite3
import sys
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

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ['setup', 'monitor']:
        print("Usage python main.py [setup|monitor]")
        sys.exit(1)

    run[sys.argv[1]]()



