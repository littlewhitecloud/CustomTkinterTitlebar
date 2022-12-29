import ctypes
from tkinter import Tk, Button, Menu, Frame, Label, X, Y, TOP, RIGHT, LEFT, FLAT
from os import getcwd
try:
	from PIL import Image, ImageTk
	from darkdetect import isDark
	from BlurWindow.blurWindow import blur
except ImportError:
	from os import system
	system(".\package.bat")
	input("Finished use latest pip to install uninstalled 3rd party library.\nProgram require restart to load library.\nPress any key to exit...")
	exit(0)
	
class CTT(Tk):
	"Custom Tkinter Titlrbar"
	def __init__(self):
		super().__init__()
		path = getcwd()
		path += "\\asset\\"

		self._t0_load = Image.open(path + 'close_50.png')
		self._t0_hov_load = Image.open(path + 'close_100.png')
		self._t0_img = ImageTk.PhotoImage(self._t0_load)
		self._t0_hov_img = ImageTk.PhotoImage(self._t0_hov_load)
		self._t1_load = Image.open(path + 'minisize_50.png')
		self._t1_hov_load = Image.open(path + 'minisize_100.png')
		self._t1_img = ImageTk.PhotoImage(self._t1_load)
		self._t1_hov_img = ImageTk.PhotoImage(self._t1_hov_load)
		self._t2_load = Image.open(path + 'fullwin_50.png')
		self._t2_hov_load = Image.open(path + 'fullwin_100.png')
		self._t2_img = ImageTk.PhotoImage(self._t2_load)
		self._t2_hov_img = ImageTk.PhotoImage(self._t2_hov_load)
		self._t3_load = Image.open(path + 'togglefull_50.png')
		self._t3_hov_load = Image.open(path + 'togglefull_100.png')
		self._t3_img = ImageTk.PhotoImage(self._t3_load)
		self._t3_hov_img = ImageTk.PhotoImage(self._t3_hov_load)

		self.w, self.h = 265, 320 # orginial window size
		self.size = None
		self.o_m = False
		self.o_f = False
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
		self.theme = "light"
		self.bg = self.colors["light"]
		self.nf = self.colors["light_nf"]
		self.fg = "dark"
		if isDark():
			self.theme = "dark"
			self.bg = self.colors["dark"]
			self.nf = self.colors["dark_nf"]
			self.fg = "light"
			self["background"] = self.colors["dark_bg"]

		self.popup = Menu(self, tearoff = 0)
		self.popup.add_command(label = "还原", command = self.resize)
		self.popup.entryconfig("还原", state="disabled")
		self.popup.add_command(label = "最小化", command = self.minsize)
		self.popup.add_command(label = "最大化", command = self.maxsize)
		self.popup.add_separator()
		self.popup.add_command(label = "关闭 (Alt+F4)", command = self.destroy)

		self.titlebar = Frame(self, bg = self.bg, height = 40)
		self._titleicon = Label(self.titlebar, bg = self.bg)
		self._titletext = Label(self.titlebar, text = "tk", bg = self.bg, fg = self.colors[self.fg])
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

		self._titleicon.pack(fill = Y, side = LEFT, padx = 6, pady = 6)
		self._titletext.pack(fill = Y, side = LEFT, padx = 1, pady = 1)

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
		self._titlemin.bind("<Enter>", self.min_on_enter)
		self._titlemin.bind("<Leave>", self.min_on_leave)
		self._titlemax.bind("<Enter>", self.max_on_enter)
		self._titlemax.bind("<Leave>", self.max_on_leave)

		self._titleicon.bind("<Button-3>", self.popupmenu)
		self.titlebar.bind("<ButtonPress-1>", self.dragging)
		self.titlebar.bind("<ButtonRelease-1>", self.stopping)
		self.titlebar.bind("<B1-Motion>", self.moving)
		self.titlebar.bind("<Double-Button-1>", self.maxsize)

		self.overrideredirect(True)
		self.geometry("%sx%s" % (self.w, self.h))
		self.iconbitmap(path + "tk.ico")
		
		GWL_EXSTYLE = -20
		WS_EX_APPWINDOW = 0x00040000
		WS_EX_TOOLWINDOW = 0x00000080
		hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
		stylew = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
		stylew = stylew & ~WS_EX_TOOLWINDOW
		stylew = stylew | WS_EX_APPWINDOW
		ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
		self.withdraw()
		self.deiconify()
		#self.addblur()
	
	def disabledo(self):
		"For disable button get event's commmand"
		pass

	def useicon(self, flag = True):
		"Show icon"
		if not flag:
			self._titleicon.pack_forget()

	def usetitle(self, flag = True):
		"Show title text"
		if not flag:
			self._titletext.pack_forget()

	def usemaxmin(self, minsize = True, maxsize = True, minshow = True, maxshow = True):
		"Show / Disable min or max button"
		if not minshow:
			self._titlemin.pack_forget()
		if not minsize:
			self.min_on_enter(None)
			self._titlemin["command"] = self.disabledo
			self._titlemin.unbind("<Leave>")
			self._titlemin.unbind("<Enter>")
		if not maxshow:
			self._titlemax.pack_forget()
		if not maxsize:
			self.max_on_enter(None)
			self._titlemax["command"] = self.disabledo
			self._titlemax.unbind("<Leave>")
			self._titlemax.unbind("<Enter>")

	def addblur(self, acrylic = True, dark = isDark()):
		"Add blur / acrylic effect to window"
		if self.theme == "dark":
			hwnd = ctypes.windll.user32.GetForegroundWindow()
			blur(hwnd = hwnd, hexColor = '#91203801',Dark = dark, Acrylic = acrylic)

	def popupmenu(self, event):
		"Popup menu"
		self.popup.post(event.x_root, event.y_root)

	def dragging(self, event):
		"Start drag window"
		global x, y
		x = event.x
		y = event.y

	def stopping(self, event):
		"Window stop"
		x = None
		y = None

	def moving(self, event):
		"Window moving"
		global x, y
		if not self.o_m:
			deltax = event.x - x
			deltay = event.y - y
			self.geometry("+%s+%s" % (self.winfo_x() + deltax, self.winfo_y() + deltay))
		else:
			self.resize()

	def focusout(self, event):
		"When focusout"
		if self.theme != "light":
			self.o_f = True
			self.titlebar["bg"] = self.nf
			self._titleicon["bg"] = self.nf
			self._titletext["bg"] = self.nf
			self._titlemin["bg"] = self.nf
			self._titlemax["bg"] = self.nf
			self._titleexit["bg"] = self.nf

	def focusin(self, event):
		"When focusin"
		if self.theme != "light":
			self.o_f = False
			self.titlebar["bg"] = self.bg
			self._titleicon["bg"] = self.bg
			self._titletext["bg"] = self.bg
			self._titlemin["bg"] = self.bg
			self._titlemax["bg"] = self.bg
			self._titleexit["bg"] = self.bg

	def resize(self):
		"Resize window"
		self.popup.entryconfig("还原", state = "disabled")
		self.popup.entryconfig("最大化", state = "active")
		self.wm_geometry("%dx%d+%d+%d" % (int(self.w), int(self.h), int(self.w_x), int(self.w_y)))
		self._titlemax["command"] = self.maxsize
		self._titlemax["image"] = self._t2_hov_img
		self.o_m = False

	def maxsize(self, event = None):
		"Maxsize Window"
		if event and self.o_m:
			self.resize()
		else:
			self.popup.entryconfig("还原", state = "active")
			self.popup.entryconfig("最大化", state = "disabled")
			self.w_x, self.w_y = self.winfo_x(), self.winfo_y()
			self.o_m = True
			self._titlemax["image"] = self._t3_hov_img
			self._titlemax["command"] = self.resize
			w, h = self.wm_maxsize()
			self.geometry("%dx%d+0+0" % (w, h - 40))
	
	def deminsize(self, event):
		"Deminsize window"
		self.focus()
		self.attributes("-alpha", 1)
	
	def minsize(self):
		"Minsize window"
		self.attributes("-alpha", 0)
		self.bind("<FocusIn>", self.deminsize)

	def exit_on_enter(self, event):
		"..."
		if not self.o_f:
			self._titleexit["background"] = self.colors["exit_fg"]
			self._titleexit["image"] = self._t0_img
		else:
			pass

	def exit_on_leave(self, event):
		"..."
		if not self.o_f:
			self._titleexit["background"] = self.bg
			self._titleexit["image"] = self._t0_hov_img
		else:
			pass

	def min_on_enter(self, event):
		"..."
		self._titlemin["image"] = self._t1_img

	def min_on_leave(self, event):
		"..."
		self._titlemin["image"] = self._t1_hov_img

	def max_on_enter(self, event):
		"..."
		if not self.o_m:
			self._titlemax["image"] = self._t2_img
		else:
			self._titlemax["image"] = self._t3_img

	def max_on_leave(self, event):
		"..."
		if not self.o_m:
			self._titlemax["image"] = self._t2_hov_img
		else:
			self._titlemax["image"] = self._t3_hov_img

	def title(self, text):
		"Rebuild tkinter's title"
		if len(text) > 15:
			self._titletext["text"] = text[:15] + "..."
		else:
			self._titletext["text"] = text
		self.wm_title(text)

	def iconbitmap(self, image):
		"Rebuild tkinter's iconbitmap"
		self._icon = Image.open(image)
		self._icon = self._icon.resize((16, 16))
		self._img = ImageTk.PhotoImage(self._icon)
		self._titleicon["image"] = self. _img
		self.wm_iconbitmap(image)

	def geometry(self, size):
		"Rebuild tkinter's geometry"
		if self.w and self.h:
			pass
		else:
			self.w, self.h = size.split('x')[0], size.split('x')[1]
		self.wm_geometry(size)

	def setgeometry(self, w, h):
		"Change the self.w and self.h forcely"
		self.w, self.h = w, h;
		self.geometry("%sx%s" % (self.w, self.h))
		
if __name__ == "__main__":
	example = CTT()
	example.geometry("690x380")
	example.mainloop()
