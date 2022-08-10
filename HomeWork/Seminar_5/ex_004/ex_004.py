# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.





def RLE_in():

    with open('HomeWork/Seminar_5/ex_004/input.txt', 'r') as f:
        x = str(f.read())

    symbol = []
    summ = []
    count = 0
    current_symbol = 0
    for i in range(0, len(x)):
        if(x[current_symbol] == x[i]):
            count = count + 1
        else:
            symbol.append(x[current_symbol])
            summ.append(count)
            count = 1
            current_symbol = i

    count = 1
    for i in range(1, len(x)):
        if(x[-i] == x[-i-1]):
            count = count + 1
        else:
            symbol.append(x[-i])
            summ.append(count)
            break

    with open('HomeWork/Seminar_5/ex_004/RLE_in.txt', 'w') as rle_in:
        for i in range(0, len(summ)):
            rle_in.write(f'{summ[i]}{symbol[i]}')

def RLE_out():
    x = 0
    with open('HomeWork/Seminar_5/ex_004/RLE_in.txt', 'r') as rle_out:
        x = rle_out.read()
    count = ''
    out = ''
    
    for i in x:
        if(i.isdigit() == True):
            count = count + i
        else:
            for j in range(0, int(count)):
                out = out + i
            count = ''
    with open('HomeWork/Seminar_5/ex_004/RLE_out.txt', 'w') as rle_out:
        rle_out.write(out)


RLE_in()
RLE_out()






    


