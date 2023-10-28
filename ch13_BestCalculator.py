import tkinter as tk

def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

win = tk.Tk()
win.title("Calculator")

entry = tk.Entry(win, width=16, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: click_button(x)
    tk.Button(win, text=button, padx=20, pady=20, font=('Arial', 20), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a Clear button
clear_button = tk.Button(win, text='C', padx=20, pady=20, font=('Arial', 20), command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=2)

# Create an Equals button
equal_button = tk.Button(win, text='=', padx=20, pady=20, font=('Arial', 20), command=calculate)
equal_button.grid(row=5, column=2, columnspan=2)

# Run the main event loop
win.mainloop()
