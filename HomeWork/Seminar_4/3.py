# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


import random

def func(a):
    a = str(a)
    b = set(a)
    list = []
    double_list = []
    x = ''
    for i in a:
        if (i in list) and (i not in double_list):
            x = x + str(i)
            double_list.append(i)
        list.append(i)
    y = set(x)
    print(f'В последовательности {a} не повторяющиеся элементы это: {b.difference(y)}')

func(random.randint(100000000, 999999999))
