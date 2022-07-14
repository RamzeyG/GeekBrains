# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def func(a):
    c = []
    while(is_number(a) == False):
        print('Неправильный ввод.')
        print('Введите пожалуйста число. Дробное число вводите через точку: ')
        a = input()
        
    b = str(a).replace(',','').replace('.','')
    for i in b:
        c.append(int(i))
    summ = 0
    for i in c:
        summ = summ + i
    
    print(f'Сумма цифр в числе {a} = {summ}')


func(input('Введите пожалуйста число.\nДробное число вводите через точку: '))
