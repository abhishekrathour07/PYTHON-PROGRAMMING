from tkinter import *
from tkinter import messagebox
win = Tk()

def hello():
    messagebox.showinfo('from computer','hello guys have a nice day')

lb = Listbox(win,fg='red')
lb.insert('1',"Python")
lb.insert('2','java')
lb.insert('3','HTML')
lb.insert('4','ruby')
lb.pack()
win.title('First')
top = Toplevel()
top.title('second')

b = Button(win,text='Greet',command=hello)
b.pack()

win.mainloop()