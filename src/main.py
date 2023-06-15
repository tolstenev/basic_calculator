from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("240x360")
win["bg"] = "grey"

calc = Entry(win, font=16)
calc.grid(row=0, column=0, columnspan=4, stick="wens", padx=1, pady=1)

Button(text="C", font=16).grid(row=1, column=0, stick="wens", padx=1, pady=1)
Button(text="CE", font=16).grid(row=1, column=1, stick="wens", padx=1, pady=1)
Button(text="+/-", font=16).grid(row=1, column=2, stick="wens", padx=1, pady=1)
Button(text="+", font=16).grid(row=1, column=3, stick="wens", padx=1, pady=1)
Button(text="-", font=16).grid(row=2, column=3, stick="wens", padx=1, pady=1)
Button(text="*", font=16).grid(row=3, column=3, stick="wens", padx=1, pady=1)
Button(text="/", font=16).grid(row=4, column=3, stick="wens", padx=1, pady=1)
Button(text=",", font=16).grid(row=5, column=1, stick="wens", padx=1, pady=1)
Button(text="=", font=16).grid(row=5, column=2, stick="wens", padx=1, pady=1, columnspan=2)

Button(text="1", font=16).grid(row=4, column=0, stick="wens", padx=1, pady=1)
Button(text="2", font=16).grid(row=4, column=1, stick="wens", padx=1, pady=1)
Button(text="3", font=16).grid(row=4, column=2, stick="wens", padx=1, pady=1)
Button(text="4", font=16).grid(row=3, column=0, stick="wens", padx=1, pady=1)
Button(text="5", font=16).grid(row=3, column=1, stick="wens", padx=1, pady=1)
Button(text="6", font=16).grid(row=3, column=2, stick="wens", padx=1, pady=1)
Button(text="7", font=16).grid(row=2, column=0, stick="wens", padx=1, pady=1)
Button(text="8", font=16).grid(row=2, column=1, stick="wens", padx=1, pady=1)
Button(text="9", font=16).grid(row=2, column=2, stick="wens", padx=1, pady=1)
Button(text="0", font=16).grid(row=5, column=0, stick="wens", padx=1, pady=1)



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