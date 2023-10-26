import os,shutil

# os.mkdir("Abhishek")

# for i in range(10):
#     os.mkdir(f"Abhishek/Language {i+1}")

# a=os.getcwd()
# print(a)
# os.chdir('Abhishek')
# b =os.getcwd()
# print(b)

# file = open("Hello.txt","x")

# file = open("Hello.txt","w")
# file.write("Hello I'm making this type of directory by the help of OS module")
# file.close()

# file = open("Hello.txt","r")
# a =file.read()
# print(a)

# for i in range(2,10):
#     os.rmdir(f"Language {i+1}")

# os.remove("Abhishek")

# if os.path.isfile("Hello.txt"):
#  os.remove("Hello.txt") 

# if os.path.isdir("Abhishek"):
#     os.rmdir("Abhishek")

# if os.path.isdir("nonempty-dir"):
#     shutil.rmtree("nonempty-dir")
import tkinter 
from tkinter import *

def update_radio():
    if var.get() == 1 and var1.get() == 2 and var2.get() == 4:
        var3.set(3)
    else:
        var3.set(0)

win = Tk()

c =Checkbutton(win,text='music',onvalue=1,offvalue=0,width=4,height=4,activebackground='green')
c.pack()
c1 = Checkbutton(win,text='playlist',onvalue=2,offvalue=0,width=4,height=4,bg='blue')
c1.pack()
c2 = Checkbutton(win,text='videos',offvalue=0,onvalue=4,width=4,height=4,activeforeground='red')
c2.pack()

var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

rb=Radiobutton(win,text='check1',width=4,height=4,activeforeground='red',value=1,variable=var, command=update_radio)
rb.pack()
rb1 = Radiobutton(win,text='check2',width=4,height=4,activeforeground='red',value=2,variable=var1, command=update_radio)
rb1.pack()
rb2 =Radiobutton(win,text='check3',width=4,height=4,value=4,variable=var2, command=update_radio)
rb2.pack()

new_rb = Radiobutton(win, text='New Radio', width=4, height=4, value=3, variable=var3)
new_rb.pack()

win.mainloop()





