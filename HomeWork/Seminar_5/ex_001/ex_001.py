# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".



def func(a):
    b = a.split(' ')
    b = [s for s in b if 'абв' not in s]

    with open('Homework/Seminar_5/ex_001/result.txt', 'w', encoding='utf-8') as r:
        for i in b:
            r.write(str(i + ' '))
        
with open('Homework/Seminar_5/ex_001/file.txt', 'r', encoding='utf-8') as f:
    a = str(f.read())
    func(a)