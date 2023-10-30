import tkinter 
from tkinter import *

win = Tk()
win.geometry("300x300")
b1 = Button(win,text="submit",activebackground='red',activeforeground='blue')
# b1.pack()
# b1.grid(row=27,column=22)
b1.place(x=200,y=120)
b2 = Button(win,text="Login",foreground="blue")
# b2.pack()
# b2.grid(row=7,column=5)
b2.place(x=120,y = 180)

win.mainloop()

# pack place button anywhere
# grid place button according to row and column
# place put button on x and y axis
