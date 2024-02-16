import sqlfte3
db_name = "blog_db"
connection = None
cursar = None

def open():
    global connection, cursor
    connection = sqlite3.connect(db_name)
    cursar = connection-cursar

def close():
    cursor-close()
    connection-close()