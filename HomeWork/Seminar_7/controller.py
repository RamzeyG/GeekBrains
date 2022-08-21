
import sqlite3
from output_data import OutFullDB, ByeBye
import input_data


        

def FindContact():
    UserInput = input('Для поиска введите Фамилию, Имя, Отчество или номер телефона:\n')
    
    conn = sqlite3.connect("Homework/Seminar_7/phonebook.db") 
    cursor = conn.cursor()
    Output = ''
    print(f'По вашему запросу найдено:\n')
    for row in cursor.execute("SELECT rowid, * FROM Phonebook"):
        
        for i in row:
            if (str(i) == str(UserInput)):
                print(f'{row}')
                Output = Output + str(i)
    if(Output == ''):
        print(f'К сожалению по запросу {UserInput} ничего не найдено')
    input_data.FuncContinue()

def DeleteContact():
    print('Выберите контакт из списка для удаления:')
    
    conn = sqlite3.connect("Homework/Seminar_7/phonebook.db") 
    cursor = conn.cursor()
    c = []
    for row in cursor.execute("SELECT rowid, * FROM Phonebook ORDER BY rowid"):
        c.append (row)
    for i in c:    
        print(i)
    cursor.close
    
    UserInput = input()
    while(UserInput.isdigit() == False):
        UserInput = input('Ошибочный ввод, пожалуйста выберите номер контакта из списка выше: \n')
        if(UserInput.isdigit() == False):
            UserInput = ' '
    conn = sqlite3.connect("Homework/Seminar_7/phonebook.db") 
    cursor = conn.cursor()
    
    cursor.execute(f"DELETE FROM phonebook WHERE rowid={int(UserInput)}")
    conn.commit()
    print('Контакт удален')
    cursor.close()
    
    input_data.FuncContinue()
    
def AddContact():
    print('Вы собираетесь добавить новый контакт. Пожалуйста введите: \n')
    SurName = input('Введите фамилию: ')
    FirstName = input('Введите имя: ')
    Patronymic = input('Введите отчество: ')
    PhoneNumber = input('Введите номер телефона: ')
    while(PhoneNumber.isdigit() == False):
        PhoneNumber = input('Номер должен состоять из цифр! Пожалуйста повторите ввод номера: ')
        if(PhoneNumber.isdigit() == False):
            PhoneNumber = ' '
    PhoneDescription = input('Введите описание номера')
    
    conn = sqlite3.connect("Homework/Seminar_7/phonebook.db") 
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Phonebook (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription) VALUES (?, ?, ?, ?, ?)", (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription))
    conn.commit()
    cursor.close()
    print(f'Контакт {SurName}, {FirstName}, {Patronymic}, {PhoneNumber}, {PhoneDescription} - добавлен в базу')
    input_data.FuncContinue()

def ImportContacts():
    with open ('Homework/Seminar_7/import.txt', 'r', encoding='utf-8') as i:
        conn = sqlite3.connect("Homework/Seminar_7/phonebook.db") 
        cursor = conn.cursor()
        
        for j in i.readlines():
            insert = j.replace('\n', '').split(',')
            
            SurName = insert[0]
            FirstName = insert[1]
            Patronymic = insert[2]
            PhoneNumber = insert[3]
            PhoneDescription = insert[4]
          
            cursor.execute("INSERT INTO Phonebook (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription) VALUES (?, ?, ?, ?, ?)", (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription))
            conn.commit()
            
        cursor.close()
        print('Импорт контактов завершен успешно')
        input_data.FuncContinue()

def ExportContacts():
    conn = sqlite3.connect("Homework/Seminar_7/phonebook.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phonebook")
    records = cursor.fetchall()
    with open('Homework/Seminar_7/export.txt', 'a', encoding='utf-8') as e:
        for i in records:
            e.write(str(i).replace('(', ')').replace(')', '') + '**')
    print('Контакты записаны в файл export.txt')
    input_data.FuncContinue()