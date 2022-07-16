# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def func(a):
    x = 0
    y = 1
    array = [0]
    for i in range(0, a):
        array.append(y)
        y = x + y
        x = y - x
    
    
    count = 1
    n = -1
   
    for i in range(0, a):
        y = int((-1)**(n+1)*array[count])
        array.insert(0, y)
        n = n - 1
        count = count + 2
        
        
    print(array)    

func(8)
func(12)