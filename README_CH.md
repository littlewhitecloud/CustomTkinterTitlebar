# 📜 _自定义标题栏_
![image](https://user-images.githubusercontent.com/71159641/208231899-c25fa950-57f7-4a90-8095-cceadbf6d371.png)
### 📃 *这是一个项目可以帮助你拥有一个自定义的标题栏！小组件可以被放到这个标题栏里面！*
#### ❔ _关于更多这个项目，我写了一篇文章在Bilibili上，它很详细的说了这个项目:  _ https://www.bilibili.com/read/cv20558473
#### *希望给我颗星~*

<p align="center">
  🌏
  <a href="README.md">English</a>
</p>


### 🎰 样例:
https://github.com/littlewhitecloud/CustomTkinterTitlebar-Examples

### 📚 _*维基*_:
#### 如果你想知道如何使用你能调用的函数的话，请访问CustomTkinterTitlebar的维基的Script部分: 
https://github.com/littlewhitecloud/CustomTkinterTitlebar/wiki/Script

### 📥 下载 :
你可以使用Pip来安装:
```batch
pip install CustomTkinterTitlebar>=1.0.7.3
```
你也可以直接从github上下载原码或查看发布

### 🖼 预览: 
https://user-images.githubusercontent.com/71159641/210712384-ebe3755a-020b-45fe-a3c0-5437a94ae917.mp4
#### 插入组件:
![image](https://user-images.githubusercontent.com/71159641/208231899-c25fa950-57f7-4a90-8095-cceadbf6d371.png)
#### 模糊:
![image](https://user-images.githubusercontent.com/71159641/215318923-521c5efd-856b-42eb-aab8-02bc5ad4727e.png)
#### 亚克力:
![image](https://user-images.githubusercontent.com/71159641/215318920-a5bce119-c343-40fd-b068-9ecbe444a60f.png)
#### 自定义图标和名称:
![image](https://user-images.githubusercontent.com/71159641/209605935-e82470ce-e0d2-4244-9299-dbcf666c7e6b.png)
![image](https://user-images.githubusercontent.com/71159641/209605940-c9c58cd9-6ff3-4455-9f7f-229611a67cda.png)
![image](https://user-images.githubusercontent.com/71159641/209605941-d38732dd-1917-42e0-985a-eba98e21494b.png)
#### 自定义最大化最小化:
![image](https://user-images.githubusercontent.com/71159641/209454983-ba0baa31-9c07-45be-8dff-47da76bf1dbf.png)
![image](https://user-images.githubusercontent.com/71159641/209454984-e3698f89-9d0d-4be1-8af3-1ca78c1068dc.png)
![image](https://user-images.githubusercontent.com/71159641/209454985-7d725083-dbcb-4856-88e4-200a34111938.png)
![image](https://user-images.githubusercontent.com/71159641/209455001-f48c076a-cac0-4310-975e-0fb64855f4cd.png)
#### 亮主题:
![image](https://user-images.githubusercontent.com/71159641/210283863-53f46392-fe74-4d4f-8939-4b42f6e96c0b.png)
![image](https://user-images.githubusercontent.com/71159641/210284157-a01117b5-2aae-44cf-89ce-be3ed027607f.png)
#### 聚焦:
![image](https://user-images.githubusercontent.com/71159641/215319002-1b6d2af9-2895-4fe2-800e-637761f08ff5.png)
#### 未聚焦:
![image](https://user-images.githubusercontent.com/71159641/215319000-31c6081d-3ab5-4ca8-9433-a8033a152aae.png)

### 📦 需求:
> - _Windows 10_
> - _Python >= 3.8.0_
> - _Tcl/Tk >= 8.6.0_
> - _Pillow >= 9.0.0_
> - _darkdetect >= 0.8.0_
> - _BlurWindow >= 1.2.1_ 如果你不用模糊，你可以不安装它
```
python -m pip install --upgrade pip
pip install pillow --user
pip install darkdetect --user
pip install BlurWindow --user 
```

### 📖 用法:
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

### 💾 支持:
#### 💻 它现在支持Windows 10 32 / 64位
> **可能也支持Windows 11, 我用的是Windows 10, 未测试过**
