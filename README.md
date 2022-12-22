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
> [ ] 亮主题时的最大化最小化和关闭按钮 (Maximize minimize and close buttons when the theme is light)
> [ ] 调整窗口大小 (Resize the window)

### 支持 (support):
#### 💻 它现在支持Windows 10 
> 可能也支持Windows 11, 我用的是Windows 10, 未测试过
#### It support Windows 10 now. 
> Maybe it also support Windows 11, I am using Windows 10, I didn't test this project on Windows 11 yet

