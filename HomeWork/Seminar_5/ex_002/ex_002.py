
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
from time import sleep

Players = ['Player_1', 'Player_2', 'Vasya_Bot']

a = 2021

def IsWin(Player, a):
    if(a == 0 or a < 0):
        print(f'\n{Player} выигрывает и забирает все конфеты себе!')
        return True
    else:
        return False

def Step(Player, a):
    print(f'\nСейчас на столе {a} конфет. Ход игрока: {Player}')
    if(Player == 'Vasya_Bot'):
        x = a%29
        if(x == 0):
            x = random.randint(1, 28)
    else:
        x = 0
        while(x not in range(1, 29)):
            try:
                x = int(input('Возьмите со стола от 1 до 28 конфет:\n'))
            except Exception as e:
                print('Так нельзя!')
                continue
    print(f'{Player} забрал {x} конфет.')
    a = a - x
    if(IsWin(Player, a) == True):
        print('Игра окончена!')
        
    else:
        Players[0], Players[1] = Players[1], Players[0]
        Step(Players[0], a)


def StartGame():
    print('Добро пожаловать в игру про конфеты!\n')

    bot = ' '
    while(bot != 'Y' and bot != 'N'):
        bot = input('Вы хотите сыграть против бота? "Y"/"N"')
        
    if(bot == 'Y'):
        Players[2], Players[1] = Players[1], Players[2]
    

    print(f'Итак! Сегодня у нас играют {Players[0]} и {Players[1]}. Кто же сделает первый ход?')
    sleep(1)
    print('В этом нам поможет великий рандом!')
    sleep(1)
    print('ииии')
    sleep(0.5)
    print('первый ход сегодня делает')
    
    choice = random.randint(0, 1)
    if(choice == 1):
        Players[0], Players[1] = Players[1], Players[0]
    sleep(1)
    print(f'{Players[0]}')

    Step(Players[0], a)



StartGame()