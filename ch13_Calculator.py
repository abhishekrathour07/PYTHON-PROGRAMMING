import tkinter
from tkinter import *
from functools import partial 

win = Tk()

def sum_numbers(Label, x1, x2):
    n1 = x1.get()
    n2 = x2.get()
    total = float(n1) + float(n2)
    Label.config(text="Sum : %.2f" % total,)

def sub_number(Label,x1,x2):
    n1= x1.get()
    n2 = x2.get()
    total = float(n1) - float(n2)
    Label.config(text= "Sub : %.2f" %total,)

def mul_number(Label,x1,x2):
    n1 = x1.get()
    n2 = x2.get()
    total =float(n1) * float(n2)
    Label.config(text='Mul : %.2f' % total,)

def div_number(Label,x1,x2):
    n1 = x1.get()
    n2 = x2.get()
    total =float(n1) / float(n2)
    Label.config(text='Div : %.2f' %total,)

l1 = Label(win, text='First no.', font=('Arial', 20))
l1.grid(row=1, column=0)

l2 = Label(win, text='Second no.', font=('Arial', 20))
l2.grid(row=2, column=0)

l = Label(win)
l.grid(row=3, column=0, columnspan=2)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win, textvariable=x1, font=('Arial', 20))
e1.grid(row=1, column=1)

e2 = Entry(win, textvariable=x2, font=('Arial', 20))
e2.grid(row=2, column=1)

sum = partial(sum_numbers, l, x1, x2)

b1 = Button(win, text='+', font=('Arial', 20), command=sum)
b1.grid(row=3, column=1)
sub = partial(sub_number,l,x1,x2)
b2 = Button(win,text='-', font=('Arial', 20),command=sub)
b2.grid(row=3,column=2)
mul = partial(mul_number,l,x1,x2)
b3 = Button(win,text='X',font=('Arial',20),command=mul)
b3.grid(row=4,column=1)
div = partial(div_number,l,x1,x2)
b4 = Button(win,text= '/',font=('Arail',20),command=div)
b4.grid(row=4,column=2)
win.mainloop()
