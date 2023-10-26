import tkinter
from tkinter import *

win = Tk()
l = Label(win,text='UserName')
l.pack()
e =Entry(win)
e.pack()
t = Text(win,width=20,height=10,foreground='blue')
t.pack()

win.mainloop()