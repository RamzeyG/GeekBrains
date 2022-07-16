# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def func(a):
    x = 0
    y = 1
    array = [0]
    for i in range(0, a):
        array.append(y)
        array.insert(0, -y)
        y = x + y
        x = y - x
    print(array)    

func(8)