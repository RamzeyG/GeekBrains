# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random

def func(a):
    array = []

    for i in range(0, a):
        x = random.randint(1, 99)
        array.append(x)

    print(f"Был создан список:\n{array}")
    
    summ = 0
    count = 1

    for i in array:
        if(count <= len(array)-1):
            summ = summ + array[count]
            count = count + 2
            
    print(f'Сумма элементов списка на нечетных позициях равна: {summ}')

func(10)