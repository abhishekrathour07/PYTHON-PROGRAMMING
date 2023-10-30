from tkinter import *

win = Tk()

l = Label(win,text='Volume',font=('Arial',20))
l.grid(row=3,column=4)

s = Scale(win,orient='horizontal',fg='red',activebackground='orange')
s.grid(row=4,column=4)

s1 = Spinbox(win,from_=0,to=20)
s1.grid(row=5,column=4)

win.mainloop()