# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def func():
    print('До какой точности рассчитыываем число Пи?')
    y = int(input('Выбирите число от 1 до 10:\n'))
    
    while(y>10 or y<0 ):
        y = int(input('Введено неверное значение.\n Пожалуйста введите число от 1 до 10:\n'))
    Pi = 0
    for i in range(0, 50):
        Pi = Pi + (1/16**i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
    print(f'Число Пи с {y} знаками после запятой: {Pi:.{y}f}')


func()