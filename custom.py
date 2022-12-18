from tkinter import Button, Tk, Frame, Label, X, Y, TOP, RIGHT, LEFT
from winreg import HKEY_CURRENT_USER as hkey, QueryValueEx as getSubkeyValue, OpenKey as getKey
from ctypes import windll
from windowblur import blur
from PIL import Image, ImageTk
from os import getcwd

def theme():
    valueMeaning = {0: "Dark", 1: "Light"}
    try:
        key = getKey(hkey, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
        subkey = getSubkeyValue(key, "AppsUseLightTheme")[0]
    except FileNotFoundError:
        return None
    return valueMeaning[subkey]

def isDark():
    if theme() is not None:
        return theme() == 'Dark'

class Tk(Tk):
	def __init__(self):
		super().__init__()
		path = getcwd()
		# resources
		self._t0_load = Image.open(path + '\\assets\\close_50.png')
		self._t0_img = ImageTk.PhotoImage(self._t0_load)

		self._t0_hov_load = Image.open(path + '\\assets\\close_100.png')
		self._t0_hov_img = ImageTk.PhotoImage(self._t0_hov_load)

		self._t1_load = Image.open(path + '\\assets\\minisize_50.png')
		self._t1_img = ImageTk.PhotoImage(self._t1_load)

		self._t1_hov_load = Image.open(path + '\\assets\\minisize_100.png')
		self._t1_hov_img = ImageTk.PhotoImage(self._t1_hov_load)

		self._t2_load = Image.open(path + '\\assets\\fullwin_50.png')
		self._t2_img = ImageTk.PhotoImage(self._t2_load)

		self._t2_hov_load = Image.open(path + '\\assets\\fullwin_100.png')
		self._t2_hov_img = ImageTk.PhotoImage(self._t2_hov_load)

		self._t3_load = Image.open(path + '\\assets\\togglefull_50.png')
		self._t3_img = ImageTk.PhotoImage(self._t3_load)

		self._t3_hov_load = Image.open(path + '\\assets\\togglefull_100.png')
		self._t3_hov_img = ImageTk.PhotoImage(self._t3_hov_load)
				
		# flags
		self.w, self.h = 0, 0
		self.o_flag = False
		self.o_m = False
		self.colors = {
			"Light": "#ffffff",
			"Dark": "#2b2b2b",
			"button_activebg": '#262626',
			"button_activefg": '#262626',
			"exit_fg": "#e81123",
			"exit_bg": "#e81123",
			"dark": "#000000",
			"dark_nf": "#2b2b2b",
			"light": "#ececee",
			"light_nf": "#ececee",
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
			
		self["background"] = self.colors[self.theme.title()]	
		# tools
		self.titlebar = Frame(self, bg = self.bg, height = 16)
		self._titleicon = Label(self.titlebar, bg = self.bg)
		self._titletext = Label(self.titlebar, text = "tk", bg = self.bg, fg = self.colors[self.fg])
		self._titlemin = Button(self.titlebar, bg = self.bg)
		self._titlemax = Button(self.titlebar, bg = self.bg)
		self._titleexit = Button(self.titlebar, bg = self.bg)
		
		# configs
		self._titleexit.config(bd = 0,
			#bg = colors["exit_fg"],
			activeforeground = self.colors["exit_fg"],
			activebackground = self.colors["exit_bg"],
			width = 44,
			image = self._t0_hov_img,
			relief = 'flat',
			command = self.quit
		)

		self._titlemin.config(bd = 0,
			#bg = colors["exit_fg"],
			activeforeground = self.colors["button_activefg"],
			activebackground = self.bg,
			width = 44,
			image = self._t1_hov_img,
			relief = 'flat',
			command = self.minsize
		)
		self._titlemax.config(bd = 0,
			#bg = colors["exit_fg"],
			activeforeground = self.colors["button_activefg"],
			activebackground = self.bg,
			width = 44,
			image = self._t2_hov_img,
			relief = 'flat',
			command = self.maxsize
		)
		
		self._titleexit.bind("<Enter>", self.exit_on_enter)
		self._titleexit.bind("<Leave>", self.exit_on_leave)
		self._titlemin.bind("<Enter>", self.min_on_enter)
		self._titlemin.bind("<Leave>", self.min_on_leave)
		self._titlemax.bind("<Enter>", self.max_on_enter)
		self._titlemax.bind("<Leave>", self.max_on_leave)
		self.bind('<FocusOut>', self.focusout)
		self.bind('<FocusIn>', self.focusin)

		self._titleicon.pack(fill = X, side = LEFT, padx = 7, pady = 7)
		self._titletext.pack(fill = X, side = LEFT, padx = 1, pady = 1)

		self._titleexit.pack(fill = Y, side = RIGHT)
		self._titlemax.pack(fill = Y, side = RIGHT)
		self._titlemin.pack(fill = Y, side = RIGHT)

		self.titlebar.pack(fill = X, side = TOP, padx = 1, pady = 1)
		# final
		self.check()
		self.titlebar.bind("<ButtonPress-1>", self.Dragging)
		self.titlebar.bind("<ButtonRelease-1>", self.Stopping)
		self.titlebar.bind("<B1-Motion>", self.Moving)
		self.titlebar.bind("<Double-Button-1>", self.maxsize)
		self.after(100, self.addblur)

	def addblur(self):
		hwnd = windll.user32.GetForegroundWindow()
		blur(hwnd = hwnd, Dark = True, Acrylic = True, AccentState = 4) # Custom AccentState
		
	def focusout(self, event):
		if self.theme != "light":
			self.titlebar["bg"] = self.nf
			self._titleicon["bg"] = self.nf
			self._titletext["bg"] = self.nf, 
			self._titlemin["bg"] = self.nf
			self._titlemax["bg"] = self.nf
			self._titleexit["bg"] = self.nf
	
	def focusin(self, event):
		if self.theme != "light":
			self.titlebar["bg"] = self.bg
			self._titleicon["bg"] = self.bg
			self._titletext["bg"] = self.bg
			self._titlemin["bg"] = self.bg
			self._titlemax["bg"] = self.bg
			self._titleexit["bg"] = self.bg

	def resizeback(self):
		#self.state("normal")
		self.wm_geometry("%dx%d" % (int(self.w), int(self.h)))
		self._titlemax["command"] = self.maxsize
		self._titlemax["image"] = self._t2_hov_img
		self.o_m = False
	
	def maxsize(self, event = None):
		if event and self.o_m == True:
			self.resizeback()
		else:
			self.o_m = True
			self._titlemax["image"] = self._t3_hov_img
			self._titlemax["command"] = self.resizeback
			w, h = self.wm_maxsize()
			self.geometry("%dx%d+0+0" % (w, h - 40))
			#self.state("zoomed")
	
	def minsize(self):
		self.overrideredirect(False)
		self.o_flag = False
		self.state("iconic")
		
	def check(self):
		if self.state() != "iconic" and self.o_flag == False:
			self.overrideredirect(True)
			self.o_flag = True
			
		self.after(500, self.check)
	
	def exit_on_enter(self, event):
		self._titleexit["background"] = self.colors["exit_fg"]
		self._titleexit["image"] = self._t0_img

	def exit_on_leave(self, event):
		self._titleexit["background"] = self.bg
		self._titleexit["image"] = self._t0_hov_img
		
	def min_on_enter(self, event):
		self._titlemin["image"] = self._t1_img

	def min_on_leave(self, event):
		self._titlemin["image"] = self._t1_hov_img

	def max_on_enter(self, event):
		if not self.o_m:
			self._titlemax["image"] = self._t2_img
		else:
			self._titlemax["image"] = self._t3_img

	def max_on_leave(self, event):
		if not self.o_m:
			self._titlemax["image"] = self._t2_hov_img
		else:
			self._titlemax["image"] = self._t3_hov_img
	
	def Dragging(self, event):
		global x, y
		x = event.x
		y = event.y

	def Stopping(self, event):
		x = None
		y = None

	def Moving(self, event):
		global x, y
		deltax = event.x - x
		deltay = event.y - y
		self.geometry("+%s+%s" % (self.winfo_x() + deltax, self.winfo_y() + deltay))
		self.update()
	
	def title(self, text):
		self._titletext["text"] = text
	
	def iconbitmap(self, photo):
		self._icon = Image.open(photo)
		self._icon = self._icon.resize((16, 16)) 
		self._img = ImageTk.PhotoImage(self._icon)
		self._titleicon["image"] = self. _img
	
	def geometry(self, size):
		if self.w and self.h:
			pass
		else:
			self.w, self.h = size.split('x')[0], size.split('x')[1]
		self.wm_geometry(size)
# Test
a = Tk()
a.title("TitleBar")
a.geometry("1030x570")
#en = Entry(a.titlebar)
#en.pack(fill = Y, expand = True, ipadx = 30, pady = 5)
a.iconbitmap("edit.png")
a.mainloop()

