# Реализуйте алгоритм перемешивания списка.

import random

def func(a):
    b = []
    if(a < 0):
        for i in range(a, 1):
            b.append(i)
    else:
        for i in range(0, a+1):
            b.append(i)
    
    print(f'Задан список:\n{b}')
    count = 0
    
    while(count<=(len(b)-1)):
        x = random.randint(count, len(b)-1)
        b[count], b[x] = b[x], b[count]
        count = count + 1
        
    # random.shuffle(b)

    print(f"Перемешанный список: \n{b}")

func(9)
func(-7)

