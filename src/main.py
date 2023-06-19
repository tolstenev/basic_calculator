from tkinter import *


def add_digit(digit):
    value = f"{calc.get()}{str(digit)}"
    calc.delete(0, END)
    calc.insert(0, value)


def delete_last_digit():
    value = calc.get()
    calc.delete(len(value)-1, len(value))


def delete_all():
    calc.delete(0, END)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.keysym == 'BackSpace':
        delete_last_digit()
    elif event.keysym == 'Delete':
        delete_all()


win = Tk()
win.title("Calculator")
win.geometry("240x360")
win["bg"] = "black"

calc = Entry(win, font=20, justify=RIGHT)
calc.grid(row=0, column=0, columnspan=4, stick="wens")

Button(text="C", font=20, bg="grey", fg="white", command=delete_last_digit).grid(row=1, column=0, stick="wens")
Button(text="CE", font=20, bg="grey", fg="white", command=delete_all).grid(row=1, column=1, stick="wens")
Button(text="+/-", font=20, bg="grey", fg="white").grid(row=1, column=2, stick="wens")
Button(text="+", font=20, bg="orange").grid(row=1, column=3, stick="wens")
Button(text="-", font=20, bg="orange").grid(row=2, column=3, stick="wens")
Button(text="*", font=20, bg="orange").grid(row=3, column=3, stick="wens")
Button(text="/", font=20, bg="orange").grid(row=4, column=3, stick="wens")
Button(text="=", font=20, bg="orange").grid(row=5, column=2, stick="wens", columnspan=2)
Button(text=",", font=20).grid(row=5, column=1, stick="wens")

Button(text="1", font=20, command=lambda: add_digit(1)).grid(row=4, column=0, stick="wens")
Button(text="2", font=20, command=lambda: add_digit(2)).grid(row=4, column=1, stick="wens")
Button(text="3", font=20, command=lambda: add_digit(3)).grid(row=4, column=2, stick="wens")
Button(text="4", font=20, command=lambda: add_digit(4)).grid(row=3, column=0, stick="wens")
Button(text="5", font=20, command=lambda: add_digit(5)).grid(row=3, column=1, stick="wens")
Button(text="6", font=20, command=lambda: add_digit(6)).grid(row=3, column=2, stick="wens")
Button(text="7", font=20, command=lambda: add_digit(7)).grid(row=2, column=0, stick="wens")
Button(text="8", font=20, command=lambda: add_digit(8)).grid(row=2, column=1, stick="wens")
Button(text="9", font=20, command=lambda: add_digit(9)).grid(row=2, column=2, stick="wens")
Button(text="0", font=20, command=lambda: add_digit(0)).grid(row=5, column=0, stick="wens")

win.bind('<Key>', press_key)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(0, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.mainloop()
