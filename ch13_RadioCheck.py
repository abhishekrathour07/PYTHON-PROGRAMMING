import tkinter 
from tkinter import *

win = Tk()

c =Checkbutton(win,text='music',onvalue=1,offvalue=0,width=4,height=4,activebackground='green')
c.pack()
c1 = Checkbutton(win,text='playlist',onvalue=1,offvalue=0,width=4,height=4,bg='blue')
c1.pack()
c2 = Checkbutton(win,text='videos',offvalue=0,onvalue=1,width=4,height=4,activeforeground='red')
c2.pack()
var = IntVar()
rb=Radiobutton(win,text='check1',width=4,height=4,activeforeground='red',value=1,variable=var)
rb.pack()
rb1 = Radiobutton(win,text='check2',width=4,height=4,activeforeground='red',value=2,variable=var)
rb1.pack()
rb2 =Radiobutton(win,text='check3',width=4,height=4,value=3,variable=var)
rb2.pack()

win.mainloop()