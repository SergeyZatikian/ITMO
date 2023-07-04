import sqlite3

try:
    con = sqlite3.connect('music.db')
    cur = con.cursor()
    con.execute("""
    CREATE TABLE IF NOT EXISTS tMusician(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    canonicalName VARCHAR(40),
    age  INTEGER,
    gender VARCHAR(20)
);
    """)

    con.execute("""
    CREATE TABLE IF NOT EXISTS tSongs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_musician INTEGER ,
    title VARCHAR(120),
    description VARCHAR(220),
    FOREIGN KEY (id_musician)  REFERENCES tMusician(id)
);
    """)

    con.execute("""
    CREATE TABLE IF NOT EXISTS tComments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_Musician INTEGER,
    id_Song INTEGER,
    textComm VARCHAR(220),
    FOREIGN KEY (id_Musician)  REFERENCES tMusician(id),
    FOREIGN KEY (id_Song)  REFERENCES tSong(id)
);
    """)

    # INSERT INTO tMusician
    # data = [('Sevak', 123, 0), ("Egor Kreed", 25, 0), ("Timati", 40, 1), ("Drake", 36, 0), ("Lady Gaga", 36, 0), ("Kanye West", 46, 0), \
    #             ('Morgenshtern', 26, 0), ('ЛСП', 28, 0), ("Дора", 23, 1)]
    # cur.executemany('INSERT INTO tMusician ( canonicalName, age, gender ) VALUES (?, ?, ?)', data)
    # INSERT INTO tSongs
    # data = [(7, "Дуло", "Танки Вертолеты" ), (8, "Безумие", "искра буря безумие" ), (2, "Где ты, где я", "Лучшая песня" )]
    # cur.executemany('INSERT INTO tSongs ( id_Musician, title, description ) VALUES (?, ?, ?)', data)
    # INSERT INTO tComments
    # data = [('супер крутой комментарий', 2, 1)]* 8
    # cur.executemany('INSERT INTO tComments ( id_Musician, id_Song, textComm) VALUES (?, ?, ?)', data)

    cur.execute('SELECT * from tMusician where gender = "w"')
    row = cur.fetchall()
    print(row)

    cur.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

finally:
    if(con):
        con.commit()
        con.close()
        print("Все сделано БОСС")