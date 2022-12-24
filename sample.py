from custom import Tk, Y
from tkinter.ttk import *
from sv_ttk import set_theme

# Test
example = Tk()
example.title("Test")
example.geometry("1030x570")
example.iconbitmap("edit.png")
set_theme("dark")

#en = Entry(example.titlebar, width = 15)
#en.pack(fill = Y)

example.mainloop()
