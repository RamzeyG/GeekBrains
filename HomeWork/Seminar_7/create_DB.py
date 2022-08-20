# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель

import sqlite3

try:
    sqlite_connection = sqlite3.connect('Homework/Seminar_7/phonebook.db')
    sqlite_create_table_query = '''CREATE TABLE Phonebook (
                                SurName TEXT NOT NULL,
                                FirstName TEXT NOT NULL,
                                Patronymic TEXT NOT NULL,
                                PhoneNumber INTEGER NOT NULL,
                                PhoneDescription TEXT NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        
        
        
conn = sqlite3.connect("phonebook.db") 
cursor = conn.cursor()
cursor.execute("INSERT INTO Phonebook (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription) VALUES (?, ?, ?, ?, ?)", ('Иванов', 'Иван', 'Иванович', 4569999945, 'домашний'))
conn.commit()
cursor.execute("INSERT INTO Phonebook (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription) VALUES (?, ?, ?, ?, ?)", ('Петров', 'Петр', 'Петрович', 455383, 'работа'))
conn.commit()
cursor.execute("INSERT INTO Phonebook (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription) VALUES (?, ?, ?, ?, ?)", ('Кузнецова', 'Лидия', 'Петровна', 7647564485, 'мобильный'))
conn.commit()
cursor.execute("INSERT INTO Phonebook (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription) VALUES (?, ?, ?, ?, ?)", ('Васильев', 'Василий', 'Васильевич', 454648665, 'работа'))
conn.commit()