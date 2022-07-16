# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

def func(a):
    array = []

    for i in range(0, a):
        x = random.randint(1, 99)
        array.append(x)

    print(f"Был создан список:\n{array}")
    
    
    summ_array = []
    count = 0
    print('\nПроизведение пар:')
    
    while(count < len(array)/2):
        summ_array.append(array[count] * array[-1-count])
        
        print(f'{array[count]} * {array[-1-count]} = {summ_array[-1]}')
        count = count + 1

func(6)

func(9)
