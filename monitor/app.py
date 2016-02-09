import sqlite3
import sys
from create_ui import build_ui

actions = {
    'setup': lambda: start_setup(),
    'monitor': lambda: start_monitoring()
}

def start_setup():
	conn = sqlite3.connect(r"services.sqlite")
	conn.execute('''CREATE TABLE if not exists SERVICES
	       (ID INT PRIMARY KEY     NOT NULL,
	       NAME           TEXT    NOT NULL,
	       URL            INT     NOT NULL,
	       DOWNTIME        CHAR(50));''')
	build_ui()

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ['setup', 'monitor']:
        print("Usage python main.py [setup|monitor]")
        sys.exit(1)

    actions[sys.argv[1]]()



