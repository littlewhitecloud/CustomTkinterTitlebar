# 自定义标题栏 CustomTkinterTitlebar
![image](https://user-images.githubusercontent.com/71159641/208231899-c25fa950-57f7-4a90-8095-cceadbf6d371.png)
##### 📖Include English & Chinese language 📜 包括英文与中文语言
### 📃 这是一个项目可以帮助你拥有一个自定义的标题栏！小组件可以被放到这个标题栏里面！(This is a project can help you to have a custom titlebar! Component can add into titlebar!)
#### 关于更多这个项目，我写了一篇文章在Bilibili上，它很详细的说了这个项目 (More about this project) ： https://www.bilibili.com/read/cv20558473

### 预览 (view) : 
https://user-images.githubusercontent.com/71159641/208288057-d02429cb-6fd3-4524-b509-bbb89b4889ab.mp4
#### 模糊 (Blur):
![image](https://user-images.githubusercontent.com/71159641/209063710-fa11556b-ca04-41db-a6d4-29b6ed3ce329.png)
#### 亚克力 (Fluent) :
![image](https://user-images.githubusercontent.com/71159641/208341143-b9d01ff0-c530-414c-be5d-38be9f55949b.png)
#### 插入组件 (insert component to titlebar) :
![image](https://user-images.githubusercontent.com/71159641/208231899-c25fa950-57f7-4a90-8095-cceadbf6d371.png)
#### 聚焦 (Focus on) :
![image](https://user-images.githubusercontent.com/71159641/208881100-3ab06ae8-f51c-459d-8d2b-8a90a6218078.png)
#### 未聚焦 (Focus out) :
![image](https://user-images.githubusercontent.com/71159641/208881104-8606a9fc-1a1e-432b-980d-16e7c7581acc.png)

### 需求 (require):
> Windows 10
> Python >= 3.8.0
> Pillow > 9.0.0 
```
python -m pip install --upgrade pip
pip install pillow --user
```

### 用法 (usage):
```
from customtkintertitlebar import Tk
from tkinter import ttk
example = Tk()
example.title("TitleBar")
example.geometry("1030x570")
en = ttk.Entry(example.titlebar)
en.pack(fill = Y, expand = True, ipadx = 30, pady = 5)
example.mainloop()
```

### 问题 (bug):
#### 我无法修复从外面导入custom.py时，发生的图片找不到的错误 (图片路径错误）
> I can not fix when I import custom.py out of the project path, it will say image not found (image path error)

### 未来添加 (features):
> - [ ] _亮主题时的最大化最小化和关闭按钮 Maximize minimize and close buttons when the theme is light_
> - [ ] _调整窗口大小 Resize the window_

### 支持 (support):
#### 💻 它现在支持Windows 10 
> 可能也支持Windows 11, 我用的是Windows 10, 未测试过
#### It support Windows 10 now. 
> Maybe it also support Windows 11, I am using Windows 10, I didn't test this project on Windows 11 yet

### 文章：
#### 整个事情的大概：
> _一个月前，我就看到有许多自定义标题栏的样例，我很羡慕。
> 于是我就在想，tkinter能不能做到呢，于是，在我一个月以前就开始挖坑了……
> 直到这一个月，我才开始去填这个坑，因为终于到了周末嘛，我把作业在周五晚上都刷完了，并且也没什么事情，闲来无事，找到了遗弃下来的这个坑，于是就开始填了……_
#### 想法：
> 先 **overrideredirect** 窗口，_使窗口失去标题栏&边框以及后面很麻烦的任务栏上的图标_。
> 然后创建一个 _Frame 设置图标，文本，最大化，最小化，关闭按钮~_
> 最后在随便完善一下，就好了。
### 理论好像存在，实践有很多问题。
#### 细节：
> - 把鼠标放在三个按钮之上的时候或显示50%透明的按钮
> - 双击标题栏会 最大化 / 最小化
> - 右键图标会有功能菜单
> - 增加 *Acrylic Blur*
> - 可拖动标题栏移动窗口
> - 可以放置任何组件 **（Menu 不可以）** 在标题栏内

开发时遇到的问题：
> 1.如何最小化
>> 直接最小化会出问题
>> 奇葩的解决办法：
先取消overrideredirect，在最小化就好了：
```
	def minsize(self):
		self.overrideredirect(False)
		self.o_flag = False # 待会再讲 o_flag什么意义
		self.state("iconic")
```		
2.最小化后再打开
会出现原标题栏
解决方案：
先检查state 是不是"iconic", 如果是，并且o_flag是假的时候
执行overrideredirect
o_flag(overrideredirect_flag): 窗口是否被overrideredirect
```
	def check(self):
		if self.state() != "iconic" and self.o_flag == False:
			self.overrideredirect(True)
			self.o_flag = True
			
		self.after(500, self.check) #每500秒刷新一次 如果你的电脑性能高的话，可以改成 100
```
3.如何移动：
```
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
```
4.最大化
直接“暴力”点：
self.state("zoomed")
但是，待会讲吧……

现存的BUG：
#1 这个版本只能使用黑暗模式，还没做光亮模式
#2 双击标题栏最大化后，最大化图标会出现问题
#3 全屏会“全屏”
#4 当有菜单的时候，菜单会在标题栏上方（推测，目前还没有试过）

修改：
2022/12/17 15:35:59
#1
不想做浅色时最大化最小化和关闭的图标了
#2 & #3 解决  + 新产生的 #5 无法正确全屏 + 新增窗口focus in（聚焦） 和 focus on（未聚焦） 时的标题栏颜色 + 自动调节主题（darkdetect） + 窗口acrylic模糊（可选，自己修改）+
优化：节约self.color[key]调用次数和os.getcwd()调用次数  + 右键窗口图标菜单
titlebar.pack取消了pady = 1, padx = 1(强迫症福音)
titleicon.pack由padx = 7, pady = 7, 改为padx = 6, pady = 6尽量和Windows原生标题栏一样大
color["light"] & color["light_nf"] 被改为淡白色#f2efef，而不是淡青色#ececee
```
from tkinter import Tk, Button, Menu, Frame, Label, X, Y, TOP, RIGHT, LEFT
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
		self.o_f = False
		self.colors = {
			"Light": "#ffffff",
			"Dark": "#2b2b2b",
			"button_activebg": '#262626',
			"button_activefg": '#262626',
			"exit_fg": "#e81123",
			"exit_bg": "#e81123",
			"dark": "#000000",
			"dark_nf": "#2b2b2b",
			"light": "#f2efef",
			"light_nf": "#f2efef",
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
		self.popup = Menu(self, tearoff = 0)
		self.popup.add_command(label = "还原", command = self.resizeback)
		self.popup.entryconfig("还原", state="disabled")
		self.popup.add_command(label = "最小化", command = self.minsize)
		self.popup.add_command(label = "最大化", command = self.maxsize)
		self.popup.add_separator()
		self.popup.add_command(label = "关闭 (Alt+F4)", command = self.destroy)
		
		self.titlebar = Frame(self, bg = self.bg)
		self._titleicon = Label(self.titlebar, bg = self.bg)
		self._titletext = Label(self.titlebar, text = "tk", bg = self.bg, fg = self.colors[self.fg])
		self._titlemin = Button(self.titlebar, bg = self.bg)
		self._titlemax = Button(self.titlebar, bg = self.bg)
		self._titleexit = Button(self.titlebar, bg = self.bg)
		
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

		self._titleicon.pack(fill = X, side = LEFT, padx = 6, pady = 6)
		self._titletext.pack(fill = X, side = LEFT, padx = 1, pady = 1)

		self._titleexit.pack(fill = Y, side = RIGHT)
		self._titlemax.pack(fill = Y, side = RIGHT)
		self._titlemin.pack(fill = Y, side = RIGHT)

		self.titlebar.pack(fill = X, side = TOP)
		
		# binds & after
		self.check()
		
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
		
		self.after(100, self.addblur)
	
	def addblur(self):
		hwnd = windll.user32.GetForegroundWindow()
		blur(hwnd = hwnd, Dark = True, Acrylic = True, AccentState = 4) # Custom AccentState
	
	def popupmenu(self, event):
		self.popup.post(event.x_root, event.y_root)
	
	def dragging(self, event):
		global x, y
		x = event.x
		y = event.y

	def stopping(self, event):
		x = None
		y = None

	def moving(self, event):
		global x, y
		if self.o_m == True:
			self.resizeback()
		else:
			deltax = event.x - x
			deltay = event.y - y
			self.geometry("+%s+%s" % (self.winfo_x() + deltax, self.winfo_y() + deltay))
			self.update()
			
	def focusout(self, event):
		if self.theme != "light":
			self.o_f = True
			self.titlebar["bg"] = self.nf
			self._titleicon["bg"] = self.nf
			self._titletext["bg"] = self.nf, 
			self._titlemin["bg"] = self.nf
			self._titlemax["bg"] = self.nf
			self._titleexit["bg"] = self.nf
	
	def focusin(self, event):
		if self.theme != "light":
			self.o_f = False
			self.titlebar["bg"] = self.bg
			self._titleicon["bg"] = self.bg
			self._titletext["bg"] = self.bg
			self._titlemin["bg"] = self.bg
			self._titlemax["bg"] = self.bg
			self._titleexit["bg"] = self.bg

	def resizeback(self):
		#self.state("normal")
		self.popup.entryconfig("还原", state = "disabled")
		self.popup.entryconfig("最大化", state = "active")
		self.wm_geometry("%dx%d+%d+%d" % (int(self.w), int(self.h), int(self.w_x), int(self.w_y)))
		self._titlemax["command"] = self.maxsize
		self._titlemax["image"] = self._t2_hov_img
		self.o_m = False
	
	def maxsize(self, event = None):
		if event and self.o_m == True:
			self.resizeback()
		else:
			self.popup.entryconfig("还原", state = "active")
			self.popup.entryconfig("最大化", state = "disabled")
			self.w_x, self.w_y = self.winfo_x(), self.winfo_y()
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
			self.addblur()
		self.after(100, self.check)
	
	def exit_on_enter(self, event):
		if not self.o_f:
			self._titleexit["background"] = self.colors["exit_fg"]
			self._titleexit["image"] = self._t0_img
		else:
			pass
			
	def exit_on_leave(self, event):
		if not self.o_f:
			self._titleexit["background"] = self.bg
			self._titleexit["image"] = self._t0_hov_img
		else:
			pass
		
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
	
	# Rewrite
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
```
