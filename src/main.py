from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("250x300")
win["bg"] = "grey"

calc = Entry(win)
calc.grid(row=0, column=0, columnspan=3)

Button(text="1").grid(row=1, column=0)
Button(text="2").grid(row=1, column=1)
Button(text="3").grid(row=1, column=2)
Button(text="4").grid(row=2, column=0)
Button(text="5").grid(row=2, column=1)
Button(text="6").grid(row=2, column=2)
Button(text="7").grid(row=3, column=0)
Button(text="8").grid(row=3, column=1)
Button(text="9").grid(row=3, column=2)
Button(text="0").grid(row=4, column=0)

win.mainloop()