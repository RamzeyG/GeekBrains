# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.

def func(a):
    b = []
    for i in range(-a, a+1):
        b.append(i)
    print(f'Задан список:\n{b}')


    print('Выберите позиции которые хотите перемножить.')
    print('Помните что нумерация позиции начинаются с 0\n')

    first_postition = int(input('Введите первую позицию:'))
    second_position = int(input('Введите вторую позицию:'))
    
    while(0> first_postition >= len(b) and 0 > second_position >=len(b)):
        print('\nУказанных позиций не существует. Пожалуста введите заного')
        first_postition = int(input('Введите первую позицию:'))
        second_position = int(input('Введите вторую позицию:'))
    
    x = b[first_postition] * b[second_position]
    
    print(f'\n{b[first_postition]} * {b[second_position]} = {x}')

func(6)

