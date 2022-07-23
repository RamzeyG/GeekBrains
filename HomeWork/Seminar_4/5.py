# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

with open('HomeWork/Seminar_4/from_ex005_file_1.txt', 'r') as f1:
    file_1 = f1.read()
with open('HomeWork/Seminar_4/from_ex005_file_2.txt', 'r') as f2:
    file_2 = f2.read()

list_2 = file_2.split('+')
list_1 = file_1.split('+')
list_number = []
file_3 = ''

print(file_1)
print(file_2)

for i in range(0, len(list_1)):

    list_number.append(int(list_1[i].split('x')[0]) + int(list_2[i].split('x')[0]))

file_3 += str(list_number[0])
for i in range(1, len(list_1)):
    file_3 += '+'+str(list_number[i])+'x^'+str(i)
    
with open('HomeWork/Seminar_4/from_ex005_file_3.txt', 'w') as f3:
    f3.write(f"{file_1} + {file_2} = {file_3.replace('^1', '')}")

print(file_3)
print(f'{file_1} + {file_2} = {file_3}')
