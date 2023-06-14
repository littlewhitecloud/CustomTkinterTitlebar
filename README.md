# _自定义标题栏_ _CustomTkinterTitlebar_
![image](https://github.com/littlewhitecloud/CustomTkinterTitlebar/assets/71159641/30f7c785-d189-4865-8095-384259e9b419)

![image](https://user-images.githubusercontent.com/71159641/209783374-f5ea3613-eb65-4ec3-9462-0eb7883d3bf9.png)
![image](https://user-images.githubusercontent.com/71159641/209128673-93a6f1db-66a6-4667-9bd7-a3c2ba096f5c.png)

### 📃 *这是一个项目可以帮助你拥有一个自定义的标题栏！小组件可以被放到这个标题栏里面* *This is a project can help you to have a custom titlebar! Widgets can add into titlebar!*
#### _关于更多这个项目，我写了一篇文章在Bilibili上，它很详细的说了这个项目_ _More about this project, I wrote an article on Bilibili, which talks about this project in more detail:_ https://www.bilibili.com/read/cv20558473
#### 如果你喜欢它，请给颗星！ leave a star if you like it!

### 预览 View: 
https://user-images.githubusercontent.com/71159641/232181268-cf20d227-d0bd-4840-9b31-fa3af150e4c8.mp4
#### 插入组件 Insert component to titlebar:
![image](https://user-images.githubusercontent.com/71159641/208231899-c25fa950-57f7-4a90-8095-cceadbf6d371.png)
#### 自定义最大化最小化 Custom minsize & maxsize:
![image](https://user-images.githubusercontent.com/71159641/209454983-ba0baa31-9c07-45be-8dff-47da76bf1dbf.png)
![image](https://user-images.githubusercontent.com/71159641/209454984-e3698f89-9d0d-4be1-8af3-1ca78c1068dc.png)
![image](https://user-images.githubusercontent.com/71159641/209454985-7d725083-dbcb-4856-88e4-200a34111938.png)
![image](https://user-images.githubusercontent.com/71159641/209455001-f48c076a-cac0-4310-975e-0fb64855f4cd.png)
#### 亮主题 Light Theme:
![image](https://user-images.githubusercontent.com/71159641/210283863-53f46392-fe74-4d4f-8939-4b42f6e96c0b.png)
![image](https://user-images.githubusercontent.com/71159641/210284157-a01117b5-2aae-44cf-89ce-be3ed027607f.png)
#### 聚焦和未聚焦 Focus in & out:
![image](https://user-images.githubusercontent.com/71159641/235348887-bfa21035-54b0-4021-8c93-4cb7d41ba11a.png)
![image](https://user-images.githubusercontent.com/71159641/235348888-8fe2de5a-d5be-42ec-ba43-f983dd93c837.png)
#### 云母 Mica:
![image](https://user-images.githubusercontent.com/86362423/235428122-334d05c2-8927-4b44-bc03-ab0ac0f1687f.png)
![image](https://user-images.githubusercontent.com/86362423/235428994-68c34c9d-1b30-4c9f-8a64-a6a760600726.png)
#### 模糊 Blur:
![image](https://user-images.githubusercontent.com/71159641/215318923-521c5efd-856b-42eb-aab8-02bc5ad4727e.png)
#### 亚克力 Fluent :
![image](https://user-images.githubusercontent.com/71159641/215318920-a5bce119-c343-40fd-b068-9ecbe444a60f.png)

### 🎰 样例 Example:
https://github.com/littlewhitecloud/CustomTkinterTitlebar-Examples

### 📚 _*维基*_ _*Wiki*_:
#### https://github.com/littlewhitecloud/CustomTkinterTitlebar/wiki/Script

### 📥 下载 Download:
你可以使用Pip来安装 You can use pip to install
```batch
pip install CustomTkinterTitlebar>=1.0.7.3
```
你也可以直接从github上下载原码或查看发布 You can also download the code from github or check the realase
### 📦 依赖 Require:
> - _Windows 10_
> - _Python >= 3.8.0_
> - _Tcl/Tk >= 8.6.0_
> - _Pillow >= 9.0.0_
> - _darkdetect >= 0.8.0_
> - _BlurWindow >= 1.2.1_
```batch
python -m pip install --upgrade pip
pip install pillow --user
pip install darkdetect --user
pip install BlurWindow --user 
```
或者只运行 Or just run
```batch
pip install CustomTkinterTitlebar --user
```

### 📖 用法 Usage:
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

### 💾 支持 Support:
#### 它现在支持 Windows 10/11 32/64 位 It support Windows 10/11 32/64 bits now.

感谢 @HuyHung1408花时间来在Windows11上测试它!
Thanks @HuyHung1408 for testing it on windows 11!
