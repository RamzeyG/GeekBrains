# -*- coding: utf-8 -*-

import telebot;
from data import BotToken
import requests
from telebot import types


data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


EUR = [data['Valute']['EUR']['Name'], data['Valute']['EUR']['Value']]
USD = [data['Valute']['USD']['Name'], data['Valute']['USD']['Value']]
GBP = ['Британский фунт', data['Valute']['GBP']['Value']]
CNY = ['Китайский юань', round(float(data['Valute']['CNY']['Value'])/10, 4)]
CHF = [data['Valute']['CHF']['Name'], data['Valute']['CHF']['Value']]
RUB = ['Российский рубль', 1]

Currency = {'EUR':EUR, 'USD':USD,'GBP':GBP,'CNY':CNY,'CHF':CHF, 'RUB':RUB}

bot = telebot.TeleBot(BotToken);



def ConvertFromTo(message):
    global NameFrom, NameTo
    
    Value = int(message.text)
    result = round(float(Currency[NameFrom][1]) * Value/float(Currency[NameTo][1]), 4)
    bot.send_message(message.chat.id, f'{Value} {NameFrom} = {result} {NameTo}')
    

def ConvertTo(message):
    markup = types.InlineKeyboardMarkup(row_width=6)
    item1 = types.InlineKeyboardButton("EUR", callback_data='toEUR')
    item2 = types.InlineKeyboardButton("USD", callback_data='toUSD')
    item3 = types.InlineKeyboardButton("GBP", callback_data='toGBP')
    item4 = types.InlineKeyboardButton("CNY", callback_data='toCNY')
    item5 = types.InlineKeyboardButton("CHF", callback_data='toCHF')
    item6 = types.InlineKeyboardButton("RUB", callback_data='toRUB')
    markup.add(item1, item2, item3, item4, item5, item6)
    
    bot.send_message(message.chat.id, f'Во что будем конвертировать?:', reply_markup=markup)
    

NameFrom = ''
NameTo = ''

    

@bot.message_handler(commands=['currency'])
    
def Questions(message):
    
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Курсы валют на сегодня:\n{Currency["EUR"][0]} - {Currency["EUR"][1]} руб.\n{Currency["USD"][0]} - {Currency["USD"][1]} руб.\n{Currency["GBP"][0]} - {Currency["GBP"][1]} руб.\n{Currency["CNY"][0]} - {Currency["CNY"][1]} руб.\n{Currency["CHF"][0]} - {Currency["CHF"][1]} руб.')
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Convert", callback_data='Convert')
    markup.add(item1)
    
    bot.send_message(message.chat.id,'Чего изволите?',reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            global NameFrom, NameTo
            if call.data == 'Convert':
                markup = types.InlineKeyboardMarkup(row_width=5)
                item1 = types.InlineKeyboardButton("EUR", callback_data='fromEUR')
                item2 = types.InlineKeyboardButton("USD", callback_data='fromUSD')
                item3 = types.InlineKeyboardButton("GBP", callback_data='fromGBP')
                item4 = types.InlineKeyboardButton("CNY", callback_data='fromCNY')
                item5 = types.InlineKeyboardButton("CHF", callback_data='fromCHF')
                item6 = types.InlineKeyboardButton("RUB", callback_data='fromRUB')
                markup.add(item1, item2, item3, item4, item5, item6)
                
                bot.send_message(call.message.chat.id, f'Что будем конвертировать?:', reply_markup=markup)
            elif call.data == 'fromEUR':
                NameFrom = 'EUR'
                ConvertTo(call.message)
            elif call.data == 'fromUSD':
                NameFrom = 'USD'
                ConvertTo(call.message)
            elif call.data == 'fromGBP':
                NameFrom = 'GBP'
                ConvertTo(call.message)
            elif call.data == 'fromCNY':
                NameFrom = 'CNY'
                ConvertTo(call.message)
            elif call.data == 'fromCHF':
                NameFrom = 'CHF'
                ConvertTo(call.message)
            elif call.data == 'fromRUB':
                NameFrom = 'RUB'
                ConvertTo(call.message)
            elif call.data == 'toEUR':
                NameTo = 'EUR'
                msg = bot.send_message(call.message.chat.id, "Введите сумму:")
                
                bot.register_next_step_handler(msg, ConvertFromTo)
            elif call.data == 'toUSD':
                NameTo = 'USD'
                msg = bot.send_message(call.message.chat.id, "Введите сумму:")
                
                bot.register_next_step_handler(msg, ConvertFromTo)
            elif call.data == 'toGBP':
                NameTo = 'GBP'
                msg = bot.send_message(call.message.chat.id, "Введите сумму:")
                
                bot.register_next_step_handler(msg, ConvertFromTo)
            elif call.data == 'toCNY':
                NameTo = 'CNY'
                msg = bot.send_message(call.message.chat.id, "Введите сумму:")
                
                bot.register_next_step_handler(msg, ConvertFromTo)
            elif call.data == 'toCHF':
                NameTo = 'CHF'
                msg = bot.send_message(call.message.chat.id, "Введите сумму:")
                
                bot.register_next_step_handler(msg, ConvertFromTo)
            elif call.data == 'toRUB':
                NameTo = 'RUB'
                msg = bot.send_message(call.message.chat.id, "Введите сумму:")
                
                bot.register_next_step_handler(msg, ConvertFromTo)
        
    except Exception as e:
        print(repr(e))

if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=60)