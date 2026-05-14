import tkinter as tk

def button_click(value):
    current = entry.get()
    if current == "Error":
       current = ""
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=5, height=2,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, height=2,
                  command=lambda b=button: button_click(b)).grid(row=row, column=col)

    col += 1

    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", width=5, height=2,
          command=clear).grid(row=row, column=0)

root.mainloop()