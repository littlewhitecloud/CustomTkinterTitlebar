from tkinter import Tk, Button, Menu, Frame, Label, X, Y, TOP, RIGHT, LEFT, FLAT
from os import getcwd
from ctypes import windll
try:
	from PIL import Image, ImageTk
	from darkdetect import isDark
	from BlurWindow.blurWindow import blur
except:
	from os import system
	system(".\build.bat")
	from PIL import Image, ImageTk
	from darkdetect import isDark
	from BlurWindow.blurWindow import blur
try:
	mw = windll.LoadLibrary(".\mw64.dll")
except OSError: # Use 32 bit
	mw = windll.LoadLibrary(".\mw32.dll")

def applywindow (window):
	""" Apply effect on the target window """
	window.overrideredirect(True)
	mw.gethwnd()
	mw.setwindow()
	window.withdraw()
	window.deiconify()
	window.focus_force()
	
class CTT(Tk):
	""" A class for custom titlebar window """
	
	def __init__(self):
		""" Class initialiser """
		super().__init__()
		self.colors = {
			"Light": "#ffffff",
			"Dark": "#2b2b2b",
			"button_activebg": "#e5e5e5",
			"button_activefg": "#e5e5e5",
			"lightexit_bg": "#f1707a",
			"darkexit_bg": "#8b0a14",
			"exit_fg": "#e81123",
			"dark": "#000000",
			"dark_nf": "#2b2b2b",
			"light": "#ffffff",
			"light_nf": "#f2efef",
			"dark_bg": "#202020"
		}
		path = getcwd() + "\\asset\\"
		if isDark():
			path += "dark\\"
			self.theme = "dark"
			self.bg = self.colors["dark"]
			self.nf = self.colors["dark_nf"]
			self.fg = "light"
			self["background"] = self.colors["dark_bg"]
		else:
			path += "light\\"
			self.theme = "light"
			self.bg = self.colors["light"]
			self.nf = self.colors["light_nf"]
			self.fg = "dark"

		self._t0_load = Image.open(path + "close_50.png")
		self._t0_hov_load = Image.open(path + "close_100.png")
		self._t0_img = ImageTk.PhotoImage(self._t0_load)
		self._t0_hov_img = ImageTk.PhotoImage(self._t0_hov_load)
		self._t1_load = Image.open(path + "minisize_50.png")
		self._t1_hov_load = Image.open(path + "minisize_100.png")
		self._t1_img = ImageTk.PhotoImage(self._t1_load)
		self._t1_hov_img = ImageTk.PhotoImage(self._t1_hov_load)
		self._t2_load = Image.open(path + "fullwin_50.png")
		self._t2_hov_load = Image.open(path + "fullwin_100.png")
		self._t2_img = ImageTk.PhotoImage(self._t2_load)
		self._t2_hov_img = ImageTk.PhotoImage(self._t2_hov_load)
		self._t3_load = Image.open(path + "togglefull_50.png")
		self._t3_hov_load = Image.open(path + "togglefull_100.png")
		self._t3_img = ImageTk.PhotoImage(self._t3_load)
		self._t3_hov_img = ImageTk.PhotoImage(self._t3_hov_load)
		self.w, self.h = 265, 320
		self.o_m = False
		self.o_f = False
		self.popup = Menu(self, tearoff = 0)
		self.popup.add_command(label = "Restore", command = self.resize)
		self.popup.add_command(label = "Minsize", command = self.minsize)
		self.popup.add_command(label = "Maxsize", command = self.maxsize)
		self.popup.add_separator()
		self.popup.add_command(label = "Close (Alt+F4)", command = self.destroy)
		self.popup.entryconfig("Restore", state = "disabled")
		
		self.titlebar = Frame(self, bg = self.bg, height = 30)
		self._titleicon = Label(self.titlebar, bg = self.bg)
		self._titletext = Label(self.titlebar, bg = self.bg, fg = self.colors[self.fg])
		self._titlemin = Button(self.titlebar, bg = self.bg)
		self._titlemax = Button(self.titlebar, bg = self.bg)
		self._titleexit = Button(self.titlebar, bg = self.bg)

		self._titleexit.config(bd = 0,
			activeforeground = self.colors["exit_fg"],
			activebackground = self.colors["%sexit_bg" % self.theme],
			width = 45,
			image = self._t0_hov_img,
			relief = FLAT,
			command = self.quit
		)
		self._titlemin.config(bd = 0,
			activeforeground = self.colors["button_activefg"],
			activebackground = self.bg,
			width = 45,
			image = self._t1_hov_img,
			relief = FLAT,
			command = self.minsize
		)
		self._titlemax.config(bd = 0,
			activeforeground = self.colors["button_activefg"],
			activebackground = self.bg,
			width = 45,
			image = self._t2_hov_img,
			relief = FLAT,
			command = self.maxsize
		)
	
		self._titleicon.pack(fill = Y, side = LEFT, padx = 5, pady = 5)
		self._titletext.pack(fill = Y, side = LEFT, pady = 1)
		self._titleexit.pack(fill = Y, side = RIGHT)
		self._titlemax.pack(fill = Y, side = RIGHT)
		self._titlemin.pack(fill = Y, side = RIGHT)
		self.titlebar.pack(fill = X, side = TOP)
		self.titlebar.pack_propagate(0)
		
		# binds & after
		self.bind("<FocusOut>", self.focusout)
		self.bind("<FocusIn>", self.focusin)
		self.bind("<F11>", self.maxsize)
		
		self._titleexit.bind("<Enter>", self.exit_on_enter)
		self._titleexit.bind("<Leave>", self.exit_on_leave)
		
		self._titleicon.bind("<Button-3>", self.popupmenu)
		self._titleicon.bind("<Double-Button-1>", self.close)
		self.titlebar.bind("<ButtonPress-1>", self.dragging)
		self.titlebar.bind("<B1-Motion>", self.moving)
		self.titlebar.bind("<Double-Button-1>", self.maxsize)
		
		self.sg("%sx%s" % (self.w, self.h))
		self.iconbitmap(".\\asset\\tk.ico")
		self.title("CTT")
		
		applywindow(self)
		
	def disabledo(self):
		""" For disalbe button get even't command """
		pass
	
	def useicon(self, flag = True):
		""" Show icon """
		if not flag:
			self._titleicon.pack_forget()
	
	def use_title(self, flag = True):
		""" Show / forget titlebar"""
		if not flag:
			self._titletext.pack_forget()
			
	def usemaxmin(self, minsize = True, maxsize = True, minshow = True, maxshow = True):
		""" Show / Disable min / max button """
		if not minshow:
			self._titlemin.pack_forget()
		elif not minsize:
			self.min_on_enter(None)
			self._titlemin["command"] = self.disabledo
			self._titlemin.unbind("<Leave>")
			self._titlemin.unbind("<Enter>")
		if not maxshow:
			self._titlemax.pack_forget()
		elif not maxsize:
			self.max_on_enter(None)
			self._titlemax["command"] = self.disabledo
			self._titlemax.unbind("<Leave>")
			self._titlemax.unbind("<Enter>")
	
	def addblur(self, acrylic = True, dark = isDark()):
		""" Add blur / acrylic effect to window """
		if dark:
			self.focus_force()
			hwnd = windll.user32.GetForegroundWindow()
			blur(hwnd = hwnd, hexColor = '#91203801',Dark = dark, Acrylic = acrylic)
	
	def popupmenu(self, event):
		""" Popup menu """
		self.popup.post(event.x_root, event.y_root)
		
	def dragging(self, event):
		""" Start drag window """
		global x, y
		x = event.x
		y = event.y

	def moving(self, event):
		""" Window moving """
		global x, y
		if not self.o_m:
			new_x, new_y = (event.x - x), (event.y - y)
			mw.moving(self.winfo_x(), self.winfo_y(), new_x, new_y)
		else:
			self.resize()

	def focusout(self, event):
		""" When focusout """
		self.exit_grey()
		self.min_grey()
		self.max_grey()
		self.o_f = True
		self.titlebar["bg"] = self.nf
		self._titleicon["bg"] = self.nf
		self._titletext["bg"] = self.nf
		self._titlemin["bg"] = self.nf
		self._titlemax["bg"] = self.nf
		self._titleexit["bg"] = self.nf

	def focusin(self, event):
		""" When focusin """
		self.o_f = False
		self.exit_back()
		self.min_back()
		self.max_back()
		self.titlebar["bg"] = self.bg
		self._titleicon["bg"] = self.bg
		self._titletext["bg"] = self.bg
		self._titlemin["bg"] = self.bg
		self._titlemax["bg"] = self.bg
		self._titleexit["bg"] = self.bg

	def resize(self):
		""" Resize window """ 
		self.popup.entryconfig("Restore", state = "disabled")
		self.popup.entryconfig("Maxsize", state = "active")
		self.wm_geometry("%dx%d+%d+%d" % (int(self.w), int(self.h), int(self.w_x), int(self.w_y)))
		self._titlemax["command"] = self.maxsize
		self._titlemax["image"] = self._t2_hov_img
		self.o_m = False

	def maxsize(self, event = None):
		""" Maxsize Window """
		if event and self.o_m:
			self.resize()
		else:
			self.popup.entryconfig("Restore", state = "active")
			self.popup.entryconfig("Maxsize", state = "disabled")
			self.w_x, self.w_y = self.winfo_x(), self.winfo_y()
			self.o_m = True
			self._titlemax["image"] = self._t3_hov_img
			self._titlemax["command"] = self.resize
			w, h = self.wm_maxsize()
			self.sg("%dx%d+0+0" % (w, h - 40))
	
	def deminsize(self, event):
		""" Deminsize window """
		self.attributes("-alpha", 1)
		self.bind("<FocusIn>", self.focusin)
		
	def minsize(self):
		""" Minsize window """
		self.attributes("-alpha", 0)
		self.bind("<FocusIn>", self.deminsize)
	
	def exit_on_enter(self, event = None):
		""" ... """
		if not self.o_f:
			self._titleexit["background"] = self.colors["exit_fg"]

	def exit_on_leave(self, event = None):
		""" Function doc """
		if not self.o_f:
			self._titleexit["background"] = self.bg

	def exit_grey(self, event = None):
		""" ... """
		self._titleexit["image"] = self._t0_img

	def exit_back(self, event = None):
		""" ... """
		self._titleexit["image"] = self._t0_hov_img
			
	def min_grey(self, event = None):
		""" ... """
		self._titlemin["image"] = self._t1_img

	def min_back(self, event = None):
		""" ... """
		self._titlemin["image"] = self._t1_hov_img

	def max_grey(self, event = None):
		""" ... """
		if not self.o_m:
			self._titlemax["image"] = self._t2_img
		else:
			self._titlemax["image"] = self._t3_img

	def max_back(self, event = None):
		""" ... """
		if not self.o_m:
			self._titlemax["image"] = self._t2_hov_img
		else:
			self._titlemax["image"] = self._t3_hov_img

	def title(self, text):
		""" Rebuild tkinter's title """
		if len(text) > 15:
			text = text[:15] + "..."
		self._titletext["text"] = text
		self.wm_title(text)

	def iconbitmap(self, image):
		""" Rebuild tkinter's iconbitmap """
		self._icon = Image.open(image)
		self._icon = self._icon.resize((16, 16))
		self._img = ImageTk.PhotoImage(self._icon)
		self._titleicon["image"] = self. _img
		self.wm_iconbitmap(image)

	def close(self, event = None):
		""" Close Window """
		self.destroy()
	
	def geometry(self, w, h):
		""" Change the self.w and self.h forcely """
		self.w, self.h = w, h
		self.sg("%sx%s" % (self.w, self.h))

	def sg(self, size):
		""" Rebuild tkinter's geometry """
		if self.w and self.h:
			pass
		else:
			self.w, self.h = size.split('x')[0], size.split('x')[1]
		self.wm_geometry(size)		
	
if __name__ == "__main__":
	example = CTT() # Test
	#example.addblur()
	example.mainloop()
