# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.



def func(a):
    b = []
    summ = 0
    for i in range(1, a+1):
        c = (1+1/i)**i
        b.append(round(c, 4))
        summ = summ + c

    print(f'Задан список {b}')
    print(f'Сумма чисел равна: {round(summ, 4)}')
    print()

func(6)

func(4)

func(12)
