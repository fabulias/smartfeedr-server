import sqlite3

DBFILE = "demo.db"
gConn = None


def init_connection():
    global gConn
    if gConn == None:
        gConn = sqlite3.connect(DBFILE, detect_types=sqlite3.PARSE_DECLTYPES)

def get_connection():
    if gConn == None:
        init_connection()
    return gConn

def close_connection():
    global gConn
    if gConn != None:
        gConn.close()
        gConn = None

def get_cursor():
    if gConn == None:
        init_connection()
    return conn.cursor()

def create_table(commit=True):
    #cur = get_cursor()
    get_connection().execute(
        '''CREATE TABLE schedule
    	(id INTEGER PRIMARY KEY AUTOINCREMENT, ration1 REAL, date1 DATE,
        ration2 REAL, date2 DATE,ration3 REAL, date3 DATE,
        ration4 REAL, date4 DATE)'''
        )

def insert_data(data):
    print ("[DATA] => ", data)
    #cur.execute("INSERT INTO foo(bar) VALUES (?)",('25/06/2003',))
    conn = get_connection()
    INSERT_CMD = "INSERT INTO schedule(ration1,date1,ration2,date2,ration3,date3,ration4,date4) VALUES (?,?,?,?,?,?,?,?)"
    do_commit = True
    conn.execute(INSERT_CMD, data)
    if do_commit:
        conn.commit()
