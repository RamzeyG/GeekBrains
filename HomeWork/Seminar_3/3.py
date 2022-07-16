# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


import random

def func(a):
    array = []

    for i in range(0, a):
        x = round(random.uniform(1, 10), 2)
        array.append(x)

    print(f"Был создан список:\n{array}")

    max_i = 0
    max_item = 0
    min_i = 1
    min_item = 0

    for i in array:
        x = str(i).split('.')
        x[0] = '0'
        x = float('.'.join(x))
        
        if(max_i < x):
            max_i = x
            max_item = i
        if(min_i > x):
            min_i = x
            min_item = i
        
    print(f'Число с максимальной дробной частью = {max_item}')
    print(f'Число с минимальной дробной частью = {min_item}')
    print(f'{max_i} - {min_i} = {max_i - min_i}')

func(5)