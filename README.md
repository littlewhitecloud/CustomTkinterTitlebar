<p align="center">
  🌏
  <a href="README_CH.md">简体中文</a>
</p>

# 📜 _CustomTkinterTitlebar_

![image](https://user-images.githubusercontent.com/71159641/208231899-c25fa950-57f7-4a90-8095-cceadbf6d371.png)
### 📃 *This is a project can help you to have a custom titlebar! Widgets can add into titlebar!*
#### ❔ More about this project, I wrote an article on Bilibili, which talks about this project in more detail: _ https://www.bilibili.com/read/cv20558473
#### *Hope got some stars~*

### 🎰 demo:
https://github.com/littlewhitecloud/CustomTkinterTitlebar-Examples

### 📚 _*wiki*_:
#### If you'd like to know how to use the functions you can call, visit the Script section of the CustomTkinterTitlebar wiki:
https://github.com/littlewhitecloud/CustomTkinterTitlebar/wiki/Script

### 📥 download:
You can use pip to install
```batch
pip install CustomTkinterTitlebar>=1.0.7.3
```
You can also download the code from github or check the realase

### View : 
https://user-images.githubusercontent.com/71159641/210712384-ebe3755a-020b-45fe-a3c0-5437a94ae917.mp4
#### insert component to titlebar:
![image](https://user-images.githubusercontent.com/71159641/208231899-c25fa950-57f7-4a90-8095-cceadbf6d371.png)
#### Blur:
![image](https://user-images.githubusercontent.com/71159641/215318923-521c5efd-856b-42eb-aab8-02bc5ad4727e.png)
#### Fluent :
![image](https://user-images.githubusercontent.com/71159641/215318920-a5bce119-c343-40fd-b068-9ecbe444a60f.png)
### icon & windowtext:
![image](https://user-images.githubusercontent.com/71159641/209605935-e82470ce-e0d2-4244-9299-dbcf666c7e6b.png)
![image](https://user-images.githubusercontent.com/71159641/209605940-c9c58cd9-6ff3-4455-9f7f-229611a67cda.png)
![image](https://user-images.githubusercontent.com/71159641/209605941-d38732dd-1917-42e0-985a-eba98e21494b.png)
#### Custom minsize & maxsize:
![image](https://user-images.githubusercontent.com/71159641/209454983-ba0baa31-9c07-45be-8dff-47da76bf1dbf.png)
![image](https://user-images.githubusercontent.com/71159641/209454984-e3698f89-9d0d-4be1-8af3-1ca78c1068dc.png)
![image](https://user-images.githubusercontent.com/71159641/209454985-7d725083-dbcb-4856-88e4-200a34111938.png)
![image](https://user-images.githubusercontent.com/71159641/209455001-f48c076a-cac0-4310-975e-0fb64855f4cd.png)
#### Light Theme:
![image](https://user-images.githubusercontent.com/71159641/210283863-53f46392-fe74-4d4f-8939-4b42f6e96c0b.png)
![image](https://user-images.githubusercontent.com/71159641/210284157-a01117b5-2aae-44cf-89ce-be3ed027607f.png)
#### Focus on:
![image](https://user-images.githubusercontent.com/71159641/215319002-1b6d2af9-2895-4fe2-800e-637761f08ff5.png)
#### Focus out:
![image](https://user-images.githubusercontent.com/71159641/215319000-31c6081d-3ab5-4ca8-9433-a8033a152aae.png)

### 📦 Require:
> - _Windows 10_
> - _Python >= 3.8.0_
> - _Tcl/Tk >= 8.6.0_
> - _Pillow >= 9.0.0_
> - _darkdetect >= 0.8.0_
> - _BlurWindow >= 1.2.1_ If you don't use blur, you can ignore it
```
python -m pip install --upgrade pip
pip install pillow --user
pip install darkdetect --user
pip install BlurWindow --user 
```

### 📖 Usage:
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

### 💾 Support:
#### It support Windows 10 32 / 64 bit now.
> **Maybe it also support Windows 11, I am using Windows 10, I didn't test this project on Windows 11 yet**
