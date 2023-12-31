from tkinter import *

win =Tk()

Menubar = Menu(win)
file = Menu(Menubar)
file.add_command(label='Open')
file.add_command(label='save')
file.add_command(label='save as')
file.add_separator()
file.add_command(label='New file')
file.add_command(label='New folder')
file.add_separator()
file.add_command(label='delete')
file.add_command(label='delete all')
file.add_separator()
file.add_command(label='exit')

edit = Menu(Menubar)
edit.add_command(label='undo')
edit.add_command(label='redo')
edit.add_separator()
edit.add_command(label='cut')
edit.add_command(label='copy')
edit.add_command(label='paste')
edit.add_separator()
edit.add_command(label='find')
edit.add_command(label='replace')
edit.add_separator()
edit.add_command(label='toggle')

Menubar.add_cascade(label='File',menu=file)
Menubar.add_cascade(label='Edit',menu = edit)
win.config(menu=Menubar)
win.mainloop()