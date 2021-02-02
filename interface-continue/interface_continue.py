from random import shuffle
from tkinter import *
from tkinter import ttk
import random
from tkinter.filedialog import *
from tkinter import scrolledtext
import sys
from tkinter.messagebox import *
import sys, fileinput


def one():
    print('sasi')

def two():
    print('sasi hui')

def three():
    pass

def four():
    pass

def five():
    pass


root=Tk()
root.geometry("500x400")
root.title('Опросник')
tabs=ttk.Notebook(root)
tabs_list=[]

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=0)
M.add_cascade(label='Вопросы',menu=m1)


tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tab5=Frame(tabs)
tabs.add(tab1,text='первый')
tabs.add(tab2,text='второй')
tabs.add(tab3,text='третий')
tabs.add(tab4,text='четвёртый')
tabs.add(tab5,text='пятый')
lbl1 = Label(tab1,)  
lbl1.grid(column=0, row=0)  
btn = Button(tab1, text="да")  
btn.grid(column=1, row=0)
btn1 = Button(tab1, text="нет")  
btn1.grid(column=2, row=0)

lbl1 = Label(tab2,)  
lbl1.grid(column=0, row=0)  
btn = Button(tab2, text="да")  
btn.grid(column=1, row=0)
btn1 = Button(tab2, text="нет")  
btn1.grid(column=2, row=0) 

lbl1 = Label(tab3,)  
lbl1.grid(column=0, row=0)  
btn = Button(tab3, text="да")  
btn.grid(column=1, row=0)
btn1 = Button(tab3, text="нет")  
btn1.grid(column=2, row=0) 

lbl1 = Label(tab4,)  
lbl1.grid(column=0, row=0)  
btn = Button(tab4, text="да")  
btn.grid(column=1, row=0)
btn1 = Button(tab4, text="нет")  
btn1.grid(column=2, row=0) 

lbl1 = Label(tab5,)  
lbl1.grid(column=0, row=0)  
btn = Button(tab5, text="да")  
btn.grid(column=1, row=0)
btn1 = Button(tab5, text="нет")  
btn1.grid(column=2, row=0) 
l1 = Label(text='mas1', font="Arial 11")
l1.config(bd=30)
l1.pack()
tabs.pack(fill='both')
root.mainloop() 







b=[]
qq=[]
gh=[]
for one in range(0, 1):
    a=input('Ввидите имя человека ')
    b.append(a)

    mas4 = [0]
    mas5 = []
    fail = open(r"C:\Users\opilane\Desktop\voprosi.txt", "r", encoding='UTF-8')
    mas1 = []
    mas2 = []
    for line in fail:
        n = line.find(",")
        mas1.append(line[0:n].strip())
        mas2.append(str(line[n+1:len(line)].strip()))
    fail.close()

    del mas1[1::2]
    del mas2[1::2]

    shuffle(mas1)
    del mas1[6:16]
    if mas1:
        print(mas1[0])
        a=input('да/нет ')
        if a!='да':
            pass
        else:
            mas4[0]+=1

    if mas1:
        print(mas1[1])
        a=input('да/нет ')
        if a!='да':
            pass
        else:
            mas4[0]+=1

    if mas1:
        print(mas1[2])
        a=input('да/нет ')
        if a!='да':
            mas4[0]+=1
        else:
            pass

    if mas1:
        print(mas1[3])
        a=input('да/нет ')
        if a!='да':
            pass
        else:
            mas4[0]+=1

    if mas1:
        print(mas1[4])
        a=input('да/нет ')
        if a!='да':
            mas4[0]+=1
        else:
            pass
    if mas4[0] >= int('3'):

        fail = open(r"C:\Users\opilane\Desktop\oiged.txt", "a", encoding='UTF-8')
        fail.write('Прошёл\n')
        fail.write(b[0])
        fail.close()

    if mas4[0] <= int('2'):

        fail = open(r"C:\Users\opilane\Desktop\valed.txt", "a", encoding='UTF-8')
        fail.write('не Прошёл\n')
        fail.write(b[0])
        fail.close()

for one in range(0, 1):
    q=input('Ввидите имя человека ')
    qq.append(q)


    mas4 = [0]
    mas5 = []
    fail = open(r"C:\Users\opilane\Desktop\voprosi.txt", "r", encoding='UTF-8')
    mas1 = []
    mas2 = []
    for line in fail:
        n = line.find(",")
        mas1.append(line[0:n].strip())
        mas2.append(str(line[n+1:len(line)].strip()))
    fail.close()

    del mas1[1::2]
    del mas2[1::2]

    shuffle(mas1)
    del mas1[6:16]
    if mas1:
        print(mas1[0])
        if q!='да':
            pass
        else:
            mas4[0]+=1

    if mas1:
        print(mas1[1])
        q=input('да/нет ')
        if q!='да':
            pass
        else:
            mas4[0]+=1

    if mas1:
        print(mas1[2])
        q=input('да/нет ')
        if q!='да':
            mas4[0]+=1
        else:
            pass

    if mas1:
        print(mas1[3])
        q=input('да/нет ')
        if q!='да':
            pass
        else:
            mas4[0]+=1

    if mas1:
        print(mas1[4])
        q=input('да/нет ')
        if q!='да':
            mas4[0]+=1
        else:
            pass
    if mas4[0] >= int('3'):

        fail = open(r"C:\Users\opilane\Desktop\oiged.txt", "a", encoding='UTF-8')
        fail.write('Прошёл\n')
        fail.write(qq[0])
        fail.close()

    if mas4[0] <= int('2'):

        fail = open(r"C:\Users\opilane\Desktop\valed.txt", "a", encoding='UTF-8')
        fail.write('не Прошёл\n')
        fail.write(qq[0])
        fail.close()
