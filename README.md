# _自定义标题栏_ _CustomTkinterTitlebar_

### 📃 *这是一个项目可以帮助你拥有一个自定义的标题栏！小组件可以被放到这个标题栏里面*

*This is a project can help you to have a custom titlebar! Widgets can add into titlebar!*

### 安装 Install
```console
pip install CustomTkinterTitlebar --user
```

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

### 预览 View
![image](https://github.com/user-attachments/assets/c04deef7-a2d2-4fb1-be19-3632e4149f6c)
![image](https://github.com/user-attachments/assets/181b8bcf-85ec-4dbc-81b2-086c36bbed11)


### 🎰 样例 Example
https://github.com/littlewhitecloud/CustomTkinterTitlebar-Examples

