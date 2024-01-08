# _自定义标题栏_ _CustomTkinterTitlebar_

### 📃 *这是一个项目可以帮助你拥有一个自定义的标题栏！小组件可以被放到这个标题栏里面* *This is a project can help you to have a custom titlebar! Widgets can add into titlebar!*

### 快速开始 Quick Start
```python
from customtitlebar import CTT
from tkinter import ttk
from sv_ttk import set_theme

example = CTT()
example.title("TitleBar")
example.geometry("1030x570")
set_theme("dark")
en = ttk.Entry(example.titlebar)
en.pack(fill = "y", expand = True, pady = 1)

example.mainloop()
```

### 预览 View:
#### 插入组件 Insert component to titlebar:

#### 亮主题 Light Theme:

#### 聚焦和未聚焦 Focus in & out:


### 🎰 样例 Example:
https://github.com/littlewhitecloud/CustomTkinterTitlebar-Examples

感谢 @HuyHung1408花时间来在Windows11上测试它!
Thanks @HuyHung1408 for testing it on windows 11!