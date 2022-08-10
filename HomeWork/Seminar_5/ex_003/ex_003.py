# Создайте программу для игры в ""Крестики-нолики"".

array = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
array_position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 9
Choise_XO = ['X', 'O']
Players = ['Игрок_1', 'Игрок_2']


def result(array):
    print(f'{array[0]} | {array[1]} | {array[2]}\n---------\n{array[3]} | {array[4]} | {array[5]}\n---------\n{array[6]} | {array[7]} | {array[8]}')

def Is_Win(Player, x):
    if((array[0] == x and array[1] == x and array[2] == x) 
    or (array[3] == x and array[4] == x and array[5] == x)
    or (array[6] == x and array[7] == x and array[8] == x)
    or (array[0] == x and array[3] == x and array[6] == x)
    or (array[1] == x and array[4] == x and array[7] == x)
    or (array[2] == x and array[5] == x and array[8] == x)
    or (array[0] == x and array[4] == x and array[8] == x)
    or (array[6] == x and array[4] == x and array[2] == x)):
        print(f'\nПоздравляем, {Player}! вы выйграли!')
        return True
    elif(count == 0):
        print('\nНичья!')
        return True
    else:
        return False


def Step(Player, x):
    global count
    print(f'\nСейчас ход: {Player} ({x}).')
    a = 0

    while(a not in array_position):
        try:
            result(array_position)
            a = int(input('Пожалуйста выберите позицию из возможных:\n'))
        except Exception as e:
            print('Позиция выбрана не верно!\n')
            continue
    
    array[a-1] = x
    array_position[a-1] = ' '
    count = count - 1

    if(Is_Win(Players[0], x) == True):
        print('Игра окончена!')
        result(array)
    else:
        Players[0], Players[1] = Players[1], Players[0]
        Choise_XO[0], Choise_XO[1] = Choise_XO[1], Choise_XO[0]
        
        print()
        result(array)
        Step(Players[0], Choise_XO[0])

print('Добро пожаловать в игру "Крестики-нолики"')
Player_choise = input('Выберите "O" или "X" для первого игрока:\n')

while(Player_choise not in Choise_XO):
    try:
        Player_choise = input('Неверный ввод!. Пожалуйста, выберите "O" или "X" для первого игрока:\n')
    except Exception as e:
        continue

if(Player_choise == 'X'):
    Choise_XO = ['X', 'O']
else:
    Choise_XO = ['O', 'X']

Step(Players[0], Choise_XO[0])








