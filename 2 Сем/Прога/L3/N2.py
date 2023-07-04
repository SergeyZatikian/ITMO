import sqlite3

# данные для запроса
data = [
    (1, 'Russia'),
    (2, 'Belarus'),
    (3, 'UK'),
    (4, 'Italy'),
    (5, 'Armenia'),
    (6, 'Greece'),
    (7, 'Portugal'),
    (8, 'Spain'),
    (9, 'USA'),
    (10, 'Germany')
]

try:
    connection = sqlite3.connect('country.db') #создать курсор для выполнения запросов
    cursor = connection.cursor()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tCountry (
            count INTEGER PRIMARY KEY,
            country VARCHAR(30)
);           
    """)

    #connection.executemany("INSERT INTO tCountry VALUES(?, ?)", data)  # добавляем с помощью множественного запроса все данные сразу

    cursor.execute('select * from tCountry')
    rows = cursor.fetchone()
    print(rows)
    rows = cursor.fetchmany(4)
    print(rows)

    # закрытькурсор
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)


finally:
    # закрыть соединение с базой
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLiteзакрыто")
connection = sqlite3.connect('country.db') #создать курсор для выполнения запросов
cursor = connection.cursor()

connection.execute("""
    CREATE TABLE IF NOT EXISTS Persons (
        count INTEGER PRIMARY KEY AUTOINCREMENT,
        names VARCHAR(30)
);           
    """)