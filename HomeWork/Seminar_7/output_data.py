import sqlite3
import input_data

def OutFullDB():
    conn = sqlite3.connect("Homework/Seminar_7/phonebook.db") 
    cursor = conn.cursor()
    c = []
    for row in cursor.execute("SELECT rowid, * FROM Phonebook ORDER BY rowid"):
        c.append (row)
    for i in c:    
        print(i)
    input_data.FuncContinue()

def ByeBye():
    print('Спасибо за обращение. Возвращайтесь еще.')

    