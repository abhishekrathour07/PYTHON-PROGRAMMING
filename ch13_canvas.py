import tkinter
from tkinter import *

win = Tk()
c = Canvas(win, width=400, height=450, bg='blue')
coord = 30, 10, 130, 230
arc = c.create_arc(coord, start=0, extent=120, fill='red')
line = c.create_oval(120,120,320,420, fill = 'orange')
c.pack()

win.mainloop()
