#  新年快乐 
# 📜 _自定义标题栏 CustomTkinterTitlebar_ <img src="https://img.shields.io/badge/Python-3.11.1-blue.svg?color=#0c63ba" alt="Python 3.11.1"/>
##### 📖Include **English** & **Chinese** language 📜 包括英文与中文语言
#### ⚠ 本程序还在预览中，可能会有许多bug! This project is still in preview, there may be many bugs!
### 😉 感谢每个看我的项目的人！Thank for everyone who looked at my project!
#### *更希望给我颗星~* *Hope got some stars~*
### 📃 *这是一个项目可以帮助你拥有一个自定义的标题栏！小组件可以被放到这个标题栏里面！(This is a project can help you to have a custom titlebar! Widgets can add into titlebar!)*
#### ❔ _关于更多这个项目，我写了一篇文章在Bilibili上，它很详细的说了这个项目 (More about this project, I wrote an article on Bilibili, which talks about this project in more detail: _ https://www.bilibili.com/read/cv20558473
> 文章其实在下面 (有删改)
### 📥 下载 (download):
你可以使用Pip来安装: (You can use pip to install):
```batch
pip install CustomTkinterTitlebar>=1.0.7.3
```
你也可以直接从github上下载原码或查看发布 (You can also download the code from github or check the realase)
### 📚 _*维基*_ _*(wiki)*_:
#### 如果你想知道如何使用你能调用的函数的话，请访问CustomTkinterTitlebar的维基的Script部分: 
(If you'd like to know how to use the functions you can call, visit the Script section of the CustomTkinterTitlebar wiki:)
https://github.com/littlewhitecloud/CustomTkinterTitlebar/wiki/Script
### 🎰 样例 (demo):
https://github.com/littlewhitecloud/CustomTkinterTitlebar-Examples
### 🖼 预览 (View) : 
https://user-images.githubusercontent.com/71159641/210712384-ebe3755a-020b-45fe-a3c0-5437a94ae917.mp4
#### 插入组件 (insert component to titlebar) :
![image](https://user-images.githubusercontent.com/71159641/208231899-c25fa950-57f7-4a90-8095-cceadbf6d371.png)
#### 模糊 (Blur):
![image](https://user-images.githubusercontent.com/71159641/209063710-fa11556b-ca04-41db-a6d4-29b6ed3ce329.png)
#### 亚克力 (Fluent) :
![image](https://user-images.githubusercontent.com/71159641/208341143-b9d01ff0-c530-414c-be5d-38be9f55949b.png)
#### 自定义图标和名称 (icon & windowtext):
![image](https://user-images.githubusercontent.com/71159641/209605935-e82470ce-e0d2-4244-9299-dbcf666c7e6b.png)
![image](https://user-images.githubusercontent.com/71159641/209605940-c9c58cd9-6ff3-4455-9f7f-229611a67cda.png)
![image](https://user-images.githubusercontent.com/71159641/209605941-d38732dd-1917-42e0-985a-eba98e21494b.png)
#### 自定义最大化最小化 (Custom minsize & maxsize)：
![image](https://user-images.githubusercontent.com/71159641/209454983-ba0baa31-9c07-45be-8dff-47da76bf1dbf.png)
![image](https://user-images.githubusercontent.com/71159641/209454984-e3698f89-9d0d-4be1-8af3-1ca78c1068dc.png)
![image](https://user-images.githubusercontent.com/71159641/209454985-7d725083-dbcb-4856-88e4-200a34111938.png)
![image](https://user-images.githubusercontent.com/71159641/209455001-f48c076a-cac0-4310-975e-0fb64855f4cd.png)
#### 亮主题 (Light Theme):
![image](https://user-images.githubusercontent.com/71159641/210283863-53f46392-fe74-4d4f-8939-4b42f6e96c0b.png)
![image](https://user-images.githubusercontent.com/71159641/210284157-a01117b5-2aae-44cf-89ce-be3ed027607f.png)
#### 聚焦 (Focus on) :
![image](https://user-images.githubusercontent.com/71159641/212060937-ab70e393-f65a-4fc5-ae77-e301fea74cd2.png)
#### 未聚焦 (Focus out) :
![image](https://user-images.githubusercontent.com/71159641/212060945-5633832d-ee07-462d-82bc-40d4afe41b25.png)

### 📦 需求 (Require):
> - _Windows 10_
> - _Python >= 3.8.0_
> - _Tcl/Tk >= 8.6.0_
> - _Pillow >= 9.0.0_
> - _darkdetect >= 0.8.0_
> - _BlurWindow >= 1.2.1_
```
python -m pip install --upgrade pip
pip install pillow --user
pip install darkdetect --user
pip install BlurWindow --user
```

### 📖 用法 (Usage):
```python
from customtkintertitlebar import Tk
from tkinter import ttk
example = Tk()
example.title("TitleBar")
example.geometry("1030x570")
en = ttk.Entry(example.titlebar)
en.pack(fill = Y, expand = True, ipadx = 30, pady = 5)
example.mainloop()
```

### 🐞 问题 (Bug):
#### _我无法修复从外面导入custom.py时，发生的图片找不到的错误 (图片路径错误）_
> I can't fix the image not found error that occurs when importing custom.py from outside (wrong picture path)

### ✨ 未来添加 (Future additions):
> - [ ] _亮主题时的最大化最小化和关闭按钮 Maximize minimize and close buttons when the theme is light_
> - [ ] _调整窗口大小 Resize the window_

### 🧊 更新(Update):
#### None

### 💾 支持 (Support):
#### 💻 它现在支持Windows 10 32 / 64位
> **可能也支持Windows 11, 我用的是Windows 10, 未测试过**
#### It support Windows 10 32 / 64 bit now.
> **Maybe it also support Windows 11, I am using Windows 10, I didn't test this project on Windows 11 yet**

## The doc doesn't support English now. I will try to translate it.
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
>> - 直接最小化会出问题
>> - 奇葩的解决办法：
>>> 先取消overrideredirect，在最小化就好了：
```python
	def minsize(self):
		self.overrideredirect(False)
		self.o_flag = False # 待会再讲 o_flag什么意义
		self.state("iconic")
```		
> 2.最小化后再打开
>> - 会出现原标题栏
>> - 解决方案：
>>> - 先检查state 是不是"iconic", 如果是，并且o_flag是假的时候执行overrideredirect
>>> - o_flag(overrideredirect_flag): 窗口是否被overrideredirect
```python
	def check(self):
		if self.state() != "iconic" and self.o_flag == False:
			self.overrideredirect(True)
			self.o_flag = True
			
		self.after(500, self.check) #每500秒刷新一次 如果你的电脑性能高的话，可以改成 100
```
> 3.如何移动：
```python
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
> 4.最大化
>> 直接“暴力”点：
>>> self.state("zoomed")

#### 现存的BUG：
> - #1 这个版本只能使用黑暗模式，还没做光亮模式
> - #2 双击标题栏最大化后，最大化图标会出现问题
> - #3 全屏会“全屏”
> - #4 当有菜单的时候，菜单会在标题栏上方
### 感谢看完这篇文档
