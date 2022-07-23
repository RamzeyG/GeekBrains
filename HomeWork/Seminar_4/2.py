# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def func_simple(a):
    count = 0
    for i in range(2, int(a)):
        if(a%i == 0):
            count = count + 1
    
    if(count == 0):
        
        return 'True'
    else:
        
        return 'False'

def simple_divisors(a):
    answer = ''
    if(func_simple(a) == 'True'):
        print(f'Число {a} не имеет простых множителей.')
    else:
        
        for i in range(a, 1, -1):
            if(i != 1 and a%i == 0 and str(func_simple(i)) == 'True'):
                answer = answer + str(i) + ', '
    print(f'Для числа {a} простые множители это: {answer[:-2]}')

simple_divisors(2520)
simple_divisors(98761)
simple_divisors(3333)
simple_divisors(12)