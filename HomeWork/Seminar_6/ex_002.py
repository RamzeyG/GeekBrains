# 2) Задача: предложить улучшения кода для уже решённых задач с помощью использования **лямбд, filter, map, zip, enumerate, array1 comprehension

import random

# 2.1 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
array = [1, 2, 3, 5, 1, 5, 3, 10]
array1 = []
double_array1 = []
def f(i):
    if (i in array1) and (i not in double_array1):
            double_array1.append(i)
            return i
    array1.append(i)

[f(i) for i in array if i != None]

unique_numbers = [i for i in [f(i) for i in array] if i != None]

print()
print('2.1 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.')
print(f'В последовательности чисел {array}\nНеповторяющиея элементы это: {unique_numbers}')

# 2.2 Найти сумму чисел списка стоящих на нечетной позиции

array = [1, 2, 3, 5, 1, 5, 3, 10]
result = 0
new_array = [array[i] for i in range(0, len(array)) if i%2 != 0]
for i in new_array:
    result = result + int(i)
print()
print('2.2 Найти сумму чисел списка стоящих на нечетной позиции')
print(f'Сумма чисел списка стоящих на нечетной позиции {new_array} равна {result}')

# 2.3 Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print()
print('2.3 Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.')
def func(n):
    print(f'Сформированный словарь для натурального n = {n}')
    print(dict(zip([i for i in range(1, n+1)], [3*i+1 for i in range(1, n+1)])))

func(random.randint(0, 30))