from tkinter import *

win =Tk()

s = Scrollbar(win)
s.pack(side=RIGHT,fill=Y)
list = Listbox(win,yscrollcommand=s.set)
for i in range(100):
    list.insert(END,'Hello everyone this is line '+str(i))
list.pack(side=LEFT,fill=BOTH)
s.config(command=list.yview)

win.mainloop()