from tkinter.ttk import Notebook
from custom import CTT, getcwd, Image, ImageTk, Button, Frame, FLAT, LEFT, X, Y, TOP
try:
	from sv_ttk import set_theme
	from darkdetect import isDark
except:
	from os import system
	system("pip install sv_ttk")
	system("pip install darkdetect")
	input("require restart to load two packages")
	exit(0)

value = 0
def newtab():
	global value
	newframe = Frame(nb, bg= "#114514")
	newframe.pack(fill = X, side = TOP)
	nb.add(newframe, text = "Tab %d" % value)
	value += 1

ex = CTT()
ex.useicon(False)
ex.usetitle(False)
ex.geometry(975, 525)
ex.titlebar["height"] = 40
if isDark():
	ex.bg = "#2f2f2f"
	ex.titlebar["background"] = "#2f2f2f"
	ex._titleexit["background"] = "#2f2f2f"
	ex._titlemin["background"] = "#2f2f2f"
	ex._titlemax["background"] = "#2f2f2f"
	set_theme("dark")
else:
	set_theme("light")
newtab_load = Image.open("newtab.png")
newtab_png = ImageTk.PhotoImage(newtab_load)
newtab = Button(ex.titlebar, image = newtab_png, command = newtab, relief = FLAT, bg = ex.bg)
nb = Notebook(ex.titlebar)
nb.pack(side = LEFT, fill = X)
nb.bind("<ButtonPress-1>", ex.dragging)
nb.bind("<B1-Motion>", ex.moving)
newtab.pack(side = LEFT, fill = Y, padx = 3, pady = 3)

ex.mainloop()
