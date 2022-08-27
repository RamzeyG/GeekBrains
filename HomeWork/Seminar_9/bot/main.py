import telebot;
import sqlite3
import csv
import os
from data import BotToken



from telebot import types
bot = telebot.TeleBot(BotToken);
DBplace = "Homework/Seminar_9//bot/phonebook.db"


@bot.message_handler(commands=['DB_connect'])
def Questions(message):
    
    markup = types.InlineKeyboardMarkup(row_width=6)
    item1 = types.InlineKeyboardButton("1", callback_data='1')
    item2 = types.InlineKeyboardButton("2", callback_data='2')
    item3 = types.InlineKeyboardButton("3", callback_data='3')
    item4 = types.InlineKeyboardButton("4", callback_data='4')
    item5 = types.InlineKeyboardButton("5", callback_data='5')
    item6 = types.InlineKeyboardButton("6", callback_data='6')
    markup.add(item1, item2, item3, item4, item5, item6)
    
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Вы подключились к базе.\nВыберите действие:\n1. Вывести список контактов.\n2. Поиск контакта.\n3. Добавление контакта.\n4. Удаление контакта.\n5. Экспорт контактов.\n6. Импорт контактов.', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    t = 'Привет' in message.text
    if t == True:
        if(message.chat.type == 'supergroup' or message.chat.type == 'group' or message.chat.type == 'private'):
           
           
           bot.send_message(message.chat.id, 'Привет!')
           markup = types.InlineKeyboardMarkup(row_width=2)
           item1 = types.InlineKeyboardButton("хорошо", callback_data='yes')
           item2 = types.InlineKeyboardButton("так себе", callback_data='no')
           markup.add(item1, item2)
           bot.send_message(message.chat.id, f'как твои дела {message.from_user.first_name}?', reply_markup=markup)
def FindContact(message):
    conn = sqlite3.connect(DBplace) 
    cursor = conn.cursor()
    Output = ''
    bot.send_message(message.chat.id, 'По вашему запросу найдено:\n')
    for row in cursor.execute("SELECT rowid, * FROM Phonebook"):
        
        for i in row:
            if (str(i) == str(message.text)):
                bot.send_message(message.chat.id, f'{row}')
                Output = Output + str(i)
    if(Output == ''):
        bot.send_message(message.chat.id, f'К сожалению по запросу {message.text} ничего не найдено')

def DeleteContact(message):
    
    UserInput = message.text
    conn = sqlite3.connect(DBplace) 
    cursor = conn.cursor()
    sql = "SELECT rowid, * FROM phonebook WHERE rowid=?"
    cursor.execute(sql, [(UserInput)])
    try:
        
        cursor.execute(f"DELETE FROM phonebook WHERE rowid={int(UserInput)}")
        conn.commit()
        bot.send_message(message.chat.id, 'Контакт удален')
        cursor.close()
            
    except TypeError: 
        bot.send_message(message.chat.id, 'Такого контакта не существует, пожалуйста повторите запрос: \n')
        
def AddContact(message):
    data = message.text.split(',')
    
    SurName = data[0]
    FirstName = data[1]
    Patronymic = data[2]
    PhoneNumber = data[3]
    
    PhoneDescription = data[4]
    
    conn = sqlite3.connect(DBplace) 
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Phonebook (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription) VALUES (?, ?, ?, ?, ?)", (SurName, FirstName, Patronymic, PhoneNumber, PhoneDescription))
    conn.commit()
    cursor.close()
    bot.send_message(message.chat.id, f'Контакт:\n {SurName}, {FirstName}, {Patronymic}, {PhoneNumber}, {PhoneDescription} - добавлен в базу')

def ExportContacts(message, format):
    conn = sqlite3.connect(DBplace) 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phonebook")
    records = cursor.fetchall()
    
    if format == 'csv':
        with open('Homework/Seminar_9/bot/export.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Фамилия', 'Имя', 'Отчество', 'Номер телефона', 'Описание'])
            spamwriter.writerows(records)
        bot.send_document(message.message.chat.id, open(r'Homework/Seminar_9/bot/export.csv', 'rb'))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'export.csv')
        os.remove(path)
    elif format == 'txt':
        with open('Homework/Seminar_9/bot/export.txt', 'a', encoding='utf-8') as e:
            for i in records:
                e.write(str(i).replace('(', ')').replace(')', '') + '\n')
    
        bot.send_document(message.message.chat.id, open(r'Homework/Seminar_9/bot/export.txt', 'rb'))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'export.txt')
        os.remove(path)
        
    
         
           


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, 'Вот и отличненько')
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, 'Ничего скоро все будет хорошо')
            elif call.data == '1':
                conn = sqlite3.connect(DBplace) 
                cursor = conn.cursor()
                i = ''
                for row in cursor.execute("SELECT * FROM Phonebook ORDER BY rowid"):
                    i = i + str(row) +'\n'
                
                bot.send_message(call.message.chat.id, i)
            elif call.data == '2':
                
                msg = bot.send_message(call.message.chat.id, 'Для поиска введите Фамилию, Имя, Отчество или номер телефона:\n')
                bot.register_next_step_handler(msg, FindContact)
                
            elif call.data == '4':
                msg = bot.send_message(call.message.chat.id, 'Выберите контакт из списка для удаления:')
    
                conn = sqlite3.connect(DBplace) 
                cursor = conn.cursor()
                i = ''
                for row in cursor.execute("SELECT rowid, * FROM Phonebook ORDER BY rowid"):
                    i = i + str(row) +'\n'
                            
                bot.send_message(call.message.chat.id, i)
                bot.register_next_step_handler(msg, DeleteContact)
            elif call.data == '3':
                msg = bot.send_message(call.message.chat.id, 'Вы собираетесь добавить новый контакт.\nПожалуйста введите Данные в формате: Фамилия, Имя, Отчество, Номер телефона, описание\nЕсли каких то данных нет, оставьте пробел между запятыми')
                bot.register_next_step_handler(msg, AddContact)
            elif call.data == '5':
                
                
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("csv", callback_data='csv')
                item2 = types.InlineKeyboardButton("txt", callback_data='txt')
                markup.add(item1, item2)
                bot.send_message(call.message.chat.id, 'В каком формате экспортируем?', reply_markup=markup)
            
            elif call.data == '6':
                bot.send_message(call.message.chat.id, 'Извините, функционал еще в разработке')
            elif call.data == 'csv':
                ExportContacts(call, 'csv')
            elif call.data == 'txt':
                ExportContacts(call, 'txt')
                    
                
                
                
                
                
        
    except Exception as e:
        print(repr(e))

       
           
if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=60)
    