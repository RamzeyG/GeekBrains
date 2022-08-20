from controller import AddContact, DeleteContact, FindContact, ImportContacts, ExportContacts
from output_data import OutFullDB, ByeBye


def Questions():
    print('Вы подключились к базе. Выберите действие:')
    print('1. Вывести список контактов.')
    print('2. Поиск контакта.')
    print('3. Добавление контакта.')
    print('4. Удаление контакта.')
    print('5. Экспорт контактов.')
    print('6. Импорт контактов.')
    x = input()
    
    if(x.isdigit() == False or x == '' or x == None):
        x = 0
    
    while(int(x) not in range(1, 7)):
        print('Неверный ввод, пожалуйста выберите действие из списка выше.')
        x = input()
        if(x.isdigit() == False or x == '' or x == None):
            x = 0
            continue
    if(x == '1'):
        OutFullDB()
    if(x == '2'):
        FindContact()
    if(x == '3'):
        AddContact()
    if(x == '4'):
        DeleteContact()
    if(x == '5'):
        ExportContacts()
    if(x == '6'):
        ImportContacts()
        
def FuncContinue():
    x = input('Ваш запрос выполнен. Хотете продолжить Y/N?')
    while(x !='Y' and x != 'N'):
        print('Неверный ввод. Вы хотите продолжить запрос? Y/N?')
        x = input()
    if(str(x) == 'Y'):
        Questions()
    elif(str(x) =='N'):
        ByeBye()
        