from tkinter import *


array = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
count = 9

def Is_Win(x):
    if((array[0] == x and array[1] == x and array[2] == x) 
    or (array[3] == x and array[4] == x and array[5] == x)
    or (array[6] == x and array[7] == x and array[8] == x)
    or (array[0] == x and array[3] == x and array[6] == x)
    or (array[1] == x and array[4] == x and array[7] == x)
    or (array[2] == x and array[5] == x and array[8] == x)
    or (array[0] == x and array[4] == x and array[8] == x)
    or (array[6] == x and array[4] == x and array[2] == x)):
        
        lbl = Label(window, text=f'Поздравляем, {textLabel[1]}! вы выйграли!', font=("Arial Bold", 14))  
        lbl.grid(column=0, row=0)
        
    elif(count == 0):
        lbl = Label(window, text=f'Ничья!', font=("Arial Bold", 14))  
        lbl.grid(column=0, row=0)
        
    else:
        return False


window = Tk()
window.title("Добро пожаловать в игру крестики-нолики!")

XO = ['X', 'O']
textLabel = ['Игрок1', 'Игрок2']

  
def ChangeStep():
    global count
    XO[0], XO[1] = XO[1], XO[0]
    textLabel[0], textLabel[1] = textLabel[1], textLabel[0]
    
    lbl = Label(window, text=f'Сейчас ходит: {textLabel[0]}', font=("Arial Bold", 14))  
    lbl.grid(column=0, row=0)
    count = count - 1
    

def click1():
    ChangeStep()
    array[0] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=2, row=0)
    Is_Win(XO[0])
def click2():
    ChangeStep()
    array[1] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=2, row=1)
    Is_Win(XO[0])
def click3():
    ChangeStep()
    array[2] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=2, row=2)
    Is_Win(XO[0])
def click4():
    ChangeStep()
    array[3] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=3, row=0)
    Is_Win(XO[0])
def click5():
    ChangeStep()
    array[4] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=3, row=1)
    Is_Win(XO[0])
def click6():
    ChangeStep()
    array[5] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=3, row=2)
    Is_Win(XO[0])
def click7():
    ChangeStep()
    array[6] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=4, row=0)
    Is_Win(XO[0])
def click8():
    ChangeStep()
    array[7] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=4, row=1)
    Is_Win(XO[0])
def click9():
    ChangeStep()
    array[8] = XO[0]
    btn = Button(window, text=XO[0])  
    btn.grid(column=4, row=2) 
    Is_Win(XO[0])    
    



window.geometry('500x500')  
lbl = Label(window, text="Сейчас ходит Игрок1", font=("Arial Bold", 14))  
lbl.grid(column=0, row=0)  
btn1 = Button(window, text=' ', height=10, width=10, command=click1)  
btn1.grid(column=2, row=0)  
btn2 = Button(window, text=' ', height=10, width=10, command=click2)  
btn2.grid(column=2, row=1)
btn3 = Button(window, text=' ', height=10, width=10, command=click3)  
btn3.grid(column=2, row=2)  
btn4 = Button(window, text=' ', height=10, width=10, command=click4)  
btn4.grid(column=3, row=0)
btn5 = Button(window, text=' ', height=10, width=10, command=click5)  
btn5.grid(column=3, row=1)  
btn6 = Button(window, text=' ', height=10, width=10, command=click6)  
btn6.grid(column=3, row=2)  
btn7 = Button(window, text=' ', height=10, width=10, command=click7)  
btn7.grid(column=4, row=0)
btn8 = Button(window, text=' ', height=10, width=10, command=click8)  
btn8.grid(column=4, row=1)  
btn9 = Button(window, text=' ', height=10, width=10, command=click9)  
btn9.grid(column=4, row=2)  

window.mainloop()

