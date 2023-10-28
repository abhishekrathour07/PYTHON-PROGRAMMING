import tkinter
from tkinter import *

win = Tk()
frame1 = Frame(win)
frame1.pack()
b1 = Button(frame1,text= 'Red',fg='red')
b1.pack(side=LEFT)
b2 = Button(frame1,text='green',fg='green')
b2.pack(side=LEFT)
b3 = Button(frame1,text='orange',fg='orange')
b3.pack(side=LEFT)

frame2 = Frame(win)
frame2.pack(side=RIGHT)
c1= Button(frame2,text='blue',fg='blue')
c1.pack(side=LEFT)
c2 = Button(frame2,text='Purple',fg='purple')
c2.pack(side=LEFT)


win.mainloop()