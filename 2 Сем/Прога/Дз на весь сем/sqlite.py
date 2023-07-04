import sqlite3

def sql (alll):
    con = sqlite3.connect(r"C://Users//36050//OneDrive//Рабочий стол//Прога//Trucks.db")
    cur = con.cursor()
    con.execute("""
        CREATE TABLE IF NOT EXISTS trucks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            weight VARCHAR(10), 
            length VARCHAR(10), 
            width VARCHAR(10), 
            height VARCHAR(10), 
            booking VARCHAR(10)
            );
        """)

    # INSter INTO tMusician
    alll
    cur.executemany('INSERT INTO trucks VALUES (?, ?, ?, ?, ?, ?)', alll)
    cur.execute('SELECT * from tMusician where gender = "w"')
    row = cur.fetchall()
    print(row)

    cur.close()
