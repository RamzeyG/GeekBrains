# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

def func(k):
    x = 'x'
    a = random.randint(0, 100)
    result = ' '+str(a)
    
    for i in range(1, k+1):
        a_n = random.randint(0, 100)
        result +='+' + str(a_n)+x+f'^{i}'
       
    with open('HomeWork/Seminar_4/from_ex004.txt', 'w') as f:
        f.write(f"{result.replace('^1', '').replace('+1x', '+x').replace(' 0+', '')}")
    
func(4)
