# Напишите программу, которая будет преобразовывать десятичное число в двоичное.



def func(a):
    b = a
    array = []
    while(b//2 >= 1):
        if(b%2 == 0):
            array.append("0")
            b = b/2
        else:
            array.append("1")
            b = (b - b%2)/2
    if(a != 0):
        array.append("1")
    else:
        array.append("0")
    array.reverse()

    print(f"DEC {a} = {''.join(array)} BIN")
    

func(8)
func(34)
func(55)
func(3)
