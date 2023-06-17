from tkinter import Tk, Button, Menu, Frame, Label, X, Y, TOP, RIGHT, LEFT, FLAT
from ctypes import windll, c_char_p, c_int, byref, sizeof
from PIL import Image, ImageTk
from darkdetect import isDark
from os import getcwd, system
from pathlib import Path

try:
	from BlurWindow.blurWindow import blur
except: # ignore it
	pass

env = Path(__file__).parent
try:
	plugin = windll.LoadLibrary(str(env / "plugin64.dll"))
except OSError: # 32 bit
	plugin = windll.LoadLibrary(str(env / "plugin32.dll"))
except FileNotFoundError:
	system("pip install CustomTkinterTitlebar --force-reinstall")

class CTT(Tk):
	""" A class for custom titlebar """
	def __init__(self, theme : str = "followsystem", unlimit: bool = False):
		""" Class initialiser """
		super().__init__()

		self.colors = {
			"light": "#ffffff", "light_nf": "#f2efef",
			"dark": "#000000", "dark_nf": "#2b2b2b", "dark_bg": "#202020",
			"button_dark_activefg": "#1a1a1a", "button_light_activefg": "#e5e5e5",
			"lightexit_bg": "#f1707a", "darkexit_bg": "#8b0a14", "exit_fg": "#e81123",
		}
		path = env / "asset"
		if theme == "followsystem":
			if isDark():
				path /= "dark"
				self.settheme("dark")
			else:
				path /= "light"
				self.settheme("light")
		else:
			path /= theme
			self.settheme(theme)

		self.close_load = Image.open(path / "close_50.png")
		self.close_hov_load = Image.open(path / "close_100.png")
		self.min_load= Image.open(path / "minisize_50.png")
		self.min_hov_load = Image.open(path / "minisize_100.png")
		self.full_load = Image.open(path / "fullwin_50.png")
		self.full_hov_load = Image.open(path / "fullwin_100.png")
		self.max_load = Image.open(path / "togglefull_50.png")
		self.max_hov_load = Image.open(path / "togglefull_100.png")
		
		self.close_img = ImageTk.PhotoImage(self.close_load)
		self.close_hov_img = ImageTk.PhotoImage(self.close_hov_load)
		self.min_img = ImageTk.PhotoImage(self.min_load)
		self.min_hov_img = ImageTk.PhotoImage(self.min_hov_load)
		self.full_img = ImageTk.PhotoImage(self.full_load)
		self.full_hov_img = ImageTk.PhotoImage(self.full_hov_load)
		self.max_img = ImageTk.PhotoImage(self.max_load)
		self.max_hov_img = ImageTk.PhotoImage(self.max_hov_load)
		
		self.width, self.height = 265, 320
		self.o_m = self.o_f = False
		self.unlimit = unlimit
		
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
			activebackground = self.colors["%sexit_bg" % self.theme],
			width = 44,
			image = self.close_hov_img,
			relief = FLAT,
			command = self.quit
		)
		self._titlemin.config(bd = 0,
			activebackground = self.colors["button_%s_activefg" % self.theme],
			width = 44,
			image = self.min_hov_img,
			relief = FLAT,
			command = self.minsize
		)
		self._titlemax.config(bd = 0,
			activebackground = self.colors["button_%s_activefg" % self.theme],
			width = 44,
			image = self.full_hov_img,
			relief = FLAT,
			command = self.maxsize
		)
		
		self.bind("<FocusOut>", self.focusout)
		self.bind("<FocusIn>", self.focusin)
		self.bind("<F11>", self.maxsize)
		
		self._titleexit.bind("<Enter>", self.exit_on_enter)
		self._titleexit.bind("<Leave>", self.exit_on_leave)
	
		self._titlemax.bind("<Enter>", self.max_grey)
		self._titlemax.bind("<Leave>", self.max_back)
		self._titlemin.bind("<Enter>", self.min_on_enter)
		self._titlemin.bind("<Leave>", self.min_on_leave)
		self._titlemax.bind("<Enter>", self.max_on_enter)
		self._titlemax.bind("<Leave>", self.max_on_leave)
	
		self._titleicon.bind("<Button-3>", self.popupmenu)
		self._titleicon.bind("<Double-Button-1>", self.close)
		self.titlebar.bind("<ButtonPress-1>", self.dragging)
		self.titlebar.bind("<B1-Motion>", self.moving)
		self.titlebar.bind("<Double-Button-1>", self.maxsize)
		
		self._titleicon.pack(fill = Y, side = LEFT, padx = 5, pady = 5)
		self._titletext.pack(fill = Y, side = LEFT, pady = 5)
		self._titleexit.pack(fill = Y, side = RIGHT)
		self._titlemax.pack(fill = Y, side = RIGHT)
		self._titlemin.pack(fill = Y, side = RIGHT)
		self.titlebar.pack(fill = X, side = TOP)
		self.titlebar.pack_propagate(0)
		self.setup()

	# Titlebar
	def titlebarconfig(self, color = {"color": None, "color_nf": None}, height = 30):
		""" Config for titlebar """
		if color["color"] and color["color_nf"]: # Require two colors : focuson & focusout
			self.bg = color["color"]
			self.nf = color["color_nf"]
			self["background"] = color["color"]
		
		if self.unlimit:
			self.titlebar["height"] = height
		else:
			if height > 30 and height <= 50:
				self.titlebar["height"] = height

		self.focusout()
		self.focusin()
		self.update()

	# Titlename
	def title(self, text):
		""" Rebuild tkinter's title """
		# TODO: show "..." if title is too long
		self._titletext["text"] = text
		self.wm_title(text)

	def title_grey(self):
		""" ... """
		self._titletext["foreground"] = "grey"

	def title_back(self):
		""" ... """
		self._titletext["foreground"] = "white"

	def usetitle(self, flag = True):
		""" Show / forget titlename """
		if not flag:
			self._titletext.pack_forget()

	def titleconfig(self, pack = "left", font = None):
		""" Config the title """
		self.usetitle(False)
		if pack == "left":
			self._titletext.pack(side = LEFT)
		elif pack == "right":
			self._titletext.pack(side = RIGHT)
		else:
			self._titletext.config(justify = "center")
			self._titletext.pack(expand = True)
		if font:
			self._titletext.config(font = font)

	# Titleicon
	def useicon(self, flag = True):
		""" Show / forget icon """
		if not flag:
			self._titleicon.pack_forget()

	def popupmenu(self, event):
		""" Popup menu """
		self.popup.post(event.x_root, event.y_root)

	def loadimage(self, image):
		""" Load image """
		self._icon = Image.open(image)
		self._icon = self._icon.resize((16, 16))
		self._img = ImageTk.PhotoImage(self._icon)
		self._titleicon["image"] = self. _img

	def iconphoto(self, image):
		""" Rebuild tkinter's iconphoto """
		self.loadimage(image)
		self.wm_iconphoto(self._img)

	def iconbitmap(self, image):
		""" Rebuild tkinter's iconbitmap """
		self.loadimage(image)
		self.wm_iconbitmap(image)

	# Titlebutton
	def exit_on_enter(self, event = None):
		""" ... """
		self._titleexit["background"] = self.colors["exit_fg"]

	def exit_on_leave(self, event = None):
		""" ... """
		if not self.o_f:
			self._titleexit["background"] = self.bg
		else:
			self._titleexit["background"] = self.nf

	def exit_grey(self, event = None):
		""" ... """
		self._titleexit["image"] = self.close_img

	def exit_back(self, event = None):
		""" ... """
		self._titleexit["image"] = self.close_hov_img

	def min_on_enter(self, event = None):
		""" ... """
		self._titlemin["background"] = self.colors["button_%s_activefg" % self.theme]

	def min_on_leave(self, event = None):
		""" ... """
		self._titlemin["background"] = self.bg

	def min_grey(self, event = None):
		""" ... """
		self._titlemin["image"] = self.min_img

	def min_back(self, event = None):
		""" ... """
		self._titlemin["image"] = self.min_hov_img

	def max_on_enter(self, event = None):
		""" ... """
		self._titlemax["background"] = self.colors["button_%s_activefg" % self.theme]

	def max_on_leave(self, event = None):
		""" ... """
		self._titlemax["background"] = self.bg

	def max_grey(self, event = None):
		""" ... """
		if not self.o_m:
			self._titlemax["image"] = self.full_img
		else:
			self._titlemax["image"] = self.max_img

	def max_back(self, event = None):
		""" ... """
		if not self.o_m:
			self._titlemax["image"] = self.full_hov_img
		else:
			self._titlemax["image"] = self.max_hov_img

	def disabledo(self):
		""" ... """
		pass

	def usemaxmin(self, minsize = True, maxsize = True, minshow = True, maxshow = True):
		""" Show / Disable min / max button """
		if not minshow:
			self._titlemin.pack_forget()
		elif not minsize:
			self.min_grey(None)
			self._titlemin["command"] = self.disabledo
			self._titlemin.unbind("<Leave>")
			self._titlemin.unbind("<Enter>")

		if not maxshow:
			self._titlemax.pack_forget()
		elif not maxsize:
			self.max_grey(None)
			self._titlemax["command"] = self.disabledo
			self._titlemax.unbind("<Leave>")
			self._titlemax.unbind("<Enter>")

	# Window functions
	def setup(self):
		""" Window Setup """
		
		self.title("CTT")
		self.geometry("%sx%s" % (self.width, self.height))
		self.iconbitmap(env / "asset" / "tk.ico")
		
		
		self.hwnd = windll.user32.FindWindowW(c_char_p(None), "CTT")
		plugin.setwindow(self.hwnd)
		#self.overrideredirect(1)
		
		self.update()
		self.focus_force()

	def moving(self, event):
		""" Window moving """
		global x, y
		if not self.o_m:
			plugin.move(self.hwnd, self.winfo_x(), self.winfo_y(), event.x - x, event.y - y) # Use C for speed
		else:
			self.resize()

	def dragging(self, event):
		""" Start drag window """
		global x, y
		x = event.x
		y = event.y

	# TODO: rewrite the maxsize function
	def maxsize(self, event = None):
		""" Maxsize Window """
		if event and self.o_m:
			self.resize()
		else:
			geometry = self.wm_geometry().split("+")[0].split("x")
			self.width, self.height = geometry[0], geometry[1]
			self.popup.entryconfig("Restore", state = "active")
			self.popup.entryconfig("Maxsize", state = "disabled")
			self.w_x, self.w_y = self.winfo_x(), self.winfo_y()
			self.o_m = True
			self._titlemax["image"] = self.max_hov_img
			self._titlemax["command"] = self.resize
			w, h = self.wm_maxsize()
			self.geometry("%dx%d-1+0" % (w - 14, h - 40))

	def resize(self):
		""" Resize window """
		self.popup.entryconfig("Restore", state = "disabled")
		self.popup.entryconfig("Maxsize", state = "active")
		self.wm_geometry("%dx%d+%d+%d" % (int(self.width), int(self.height), int(self.w_x), int(self.w_y)))
		self._titlemax["command"] = self.maxsize
		self._titlemax["image"] = self.full_hov_img
		self.o_m = False

	def minsize(self):
		""" Minsize window """
		self.attributes("-alpha", 0)
		self.bind("<FocusIn>", self.deminsize)

	def deminsize(self, event):
		""" Deminsize window """
		self.attributes("-alpha", 1)
		self.bind("<FocusIn>", self.focusin)
	
	def setcolor(self, status, color):
		if status == "out":
			self.exit_grey()
			self.min_grey()
			self.max_grey()
			self.title_grey()
			self.o_f = True
			
		else:
			self.exit_back()
			self.min_back()
			self.max_back()
			self.title_back()
			self.o_f = False
		
			if self.theme == "followsystem" or self.theme == "light":
				self._titletext["fg"] = self.colors[self.fg]
			
		self.titlebar["bg"] = color
		self._titletext["bg"] = color
		self._titleicon["bg"] = color
		self._titlemin["bg"] = color
		self._titlemax["bg"] = color
		self._titleexit["bg"] = color
	
	def focusout(self, event = None):
		""" When focusout """
		self.setcolor("out", self.nf)

	def focusin(self, event = None):
		""" When focusin """
		self.setcolor("in", self.bg)
		
	def useblur(self, acrylic = True, dark = isDark()):
		""" Add blur / acrylic effect to window """
		if dark and self.theme != "light":
			blur(hwnd = self.hwnd, hexColor = '#19191800', Dark = dark, Acrylic = acrylic)

	def close(self, event = None):
		""" Close Window """
		self.destroy()

	def sg(self, w, h):
		""" Change the self.w and self.h forcely """
		self.width, self.height = w, h
		self.geometry("%sx%s" % (self.width, self.height))

	def geometry(self, size):
		""" Rebuild tkinter's geometry """
		if self.width and self.height:
			pass
		else:
			self.width, self.height = size.split('x')[0], size.split('x')[1]
		self.wm_geometry(size)

	def settheme(self, theme):
		""" Set the window's theme """
		if theme == "dark":
			self.theme = "dark"
			self.bg = self.colors["dark"]
			self.nf = self.colors["dark_nf"]
			self.fg = "light"
			self["background"] = self.colors["dark_bg"]
			
			self.update()
			windll.dwmapi.DwmSetWindowAttribute(windll.user32.GetParent(self.winfo_id()), 20, byref(c_int(2)), sizeof(c_int(2)))
			self.update()
		else:
			self.theme = "light"
			self.bg = self.colors["light"]
			self.nf = self.colors["light_nf"]
			self.fg = "dark"
			self.update()
