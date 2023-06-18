from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("240x360")
win["bg"] = "black"

calc = Entry(win, font=20)
calc.grid(row=0, column=0, columnspan=4, stick="wens")


Button(text="C", font=20, bg="grey", fg="white").grid(row=1, column=0, stick="wens")
Button(text="CE", font=20, bg="grey", fg="white").grid(row=1, column=1, stick="wens")
Button(text="+/-", font=20, bg="grey", fg="white").grid(row=1, column=2, stick="wens")
Button(text="+", font=20, bg="orange").grid(row=1, column=3, stick="wens")
Button(text="-", font=20, bg="orange").grid(row=2, column=3, stick="wens")
Button(text="*", font=20, bg="orange").grid(row=3, column=3, stick="wens")
Button(text="/", font=20, bg="orange").grid(row=4, column=3, stick="wens")
Button(text="=", font=20, bg="orange").grid(row=5, column=2, stick="wens", columnspan=2)
Button(text=",", font=20).grid(row=5, column=1, stick="wens")

Button(text="1", font=20).grid(row=4, column=0, stick="wens")
Button(text="2", font=20).grid(row=4, column=1, stick="wens")
Button(text="3", font=20).grid(row=4, column=2, stick="wens")
Button(text="4", font=20).grid(row=3, column=0, stick="wens")
Button(text="5", font=20).grid(row=3, column=1, stick="wens")
Button(text="6", font=20).grid(row=3, column=2, stick="wens")
Button(text="7", font=20).grid(row=2, column=0, stick="wens")
Button(text="8", font=20).grid(row=2, column=1, stick="wens")
Button(text="9", font=20).grid(row=2, column=2, stick="wens")
Button(text="0", font=20).grid(row=5, column=0, stick="wens")

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