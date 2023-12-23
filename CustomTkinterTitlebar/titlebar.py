"""A special window for custom titlebar"""
from ctypes import c_char_p, windll, WINFUNCTYPE, c_uint64
from pathlib import Path
from tkinter import FLAT, LEFT, RIGHT, TOP, Button, Frame, Label, Menu, Tk, X, Y, Event
from ctypes.wintypes import HWND, MSG, WPARAM, LPARAM
from darkdetect import isDark
from PIL import Image, ImageTk
from data import *

env = Path(__file__).parent
try:
    plugin = windll.LoadLibrary(str(env / "plugin64.dll"))
except OSError:  # 32 bit
    plugin = windll.LoadLibrary(str(env / "plugin32.dll"))


class CTT(Tk):
    """Custom Tkinter Titlebar Window Class"""

    def __init__(self, theme: str = "auto", unlimit: bool = False):
        """Class initialiser"""
        super().__init__()

        self.colors = {
            "light": "#ffffff",
            "light_nf": "#f2efef",
            "dark": "#000000",
            "dark_nf": "#2b2b2b",
            "dark_bg": "#202020",
            "button_dark_activefg": "#1a1a1a",
            "button_light_activefg": "#e5e5e5",
            "lightexit_bg": "#f1707a",
            "darkexit_bg": "#8b0a14",
            "exit_fg": "#e81123",
        }

        self.theme = ("dark" if isDark() else "light") if theme == "auto" else theme
        self.settheme(self.theme)
        self.path = env / "asset" / self.theme

        self.close_img = ImageTk.PhotoImage(Image.open(self.path / "close_50.png"))
        self.min_img = ImageTk.PhotoImage(Image.open(self.path / "minisize_50.png"))
        self.full_img = ImageTk.PhotoImage(Image.open(self.path / "fullwin_50.png"))
        self.max_img = ImageTk.PhotoImage(Image.open(self.path / "togglefull_50.png"))
        self.close_hov_img = ImageTk.PhotoImage(Image.open(self.path / "close_100.png"))
        self.min_hov_img = ImageTk.PhotoImage(Image.open(self.path / "minisize_100.png"))
        self.full_hov_img = ImageTk.PhotoImage(Image.open(self.path / "fullwin_100.png"))
        self.max_hov_img = ImageTk.PhotoImage(Image.open(self.path / "togglefull_100.png"))

        self.width, self.height = 265, 320
        self.fullscreen = self.focus = False
        self.unlimit = unlimit

        self.popup = Menu(self, tearoff=0)
        self.popup.add_command(label="Restore", command=self.resize)
        self.popup.add_command(label="Minsize", command=self.minsize)
        self.popup.add_command(label="Maxsize", command=self.maxsize)
        self.popup.add_separator()
        self.popup.add_command(label="Close (Alt+F4)", command=self.destroy)
        self.popup.entryconfig("Restore", state="disabled")

        self.titlebar = Frame(self, bg=self.bg, height=30)
        self.icon = Label(self.titlebar, bg=self.bg)
        self.text = Label(self.titlebar, bg=self.bg, fg=self.colors[self.fg])
        self.min =  Button(self.titlebar, bg=self.bg, bd=0, width=44, relief=FLAT)
        self.max = Button(self.titlebar, bg=self.bg, bd=0, width=44, relief=FLAT)
        self.exit = Button(self.titlebar, bg=self.bg, bd=0, width=44, relief=FLAT)

        self.exit.config(
            activebackground=self.colors["%sexit_bg" % self.theme],
            image=self.close_hov_img,
            command=self.quit,
        )
        self.min.config(
            activebackground=self.colors["button_%s_activefg" % self.theme],
            image=self.min_hov_img,
            command=self.minsize,
        )
        self.max.config(
            activebackground=self.colors["button_%s_activefg" % self.theme],
            image=self.full_hov_img,
            command=self.maxsize,
        )

        self.bind("<FocusOut>", self.focusout)
        self.bind("<FocusIn>", self.focusin)

        self.exit.bind("<Enter>", \
            lambda _: self.exit.config(background = self.colors["exit_fg"]))
        self.exit.bind("<Leave>", \
            lambda _: self.exit.config(background = self.nf if self.focus else self.bg))

        self.max.bind("<Enter>", \
            lambda _: self.max.config(image = self.full_img if self.fullscreen else self.max_img))
        self.max.bind("<Leave>", \
            lambda _: self.max(image = sellf.full_hov_img if self.fullscreen else self.max_hov_img))
        self.min.bind("<Enter>", \
            lambda _: self.min.config(background = self.colors["button_%s_activefg" % self.theme]))
        self.min.bind("<Leave>", lambda _: self.min.config(background = self.bg))
        self.max.bind("<Enter>", \
            lambda _: self.max.config(background = self.colors["button_%s_activefg" % self.theme]))
        self.max.bind("<Leave>", lambda _: self.max.config(background = self.bg))

        
        self.icon.bind("<Double-Button-1>", self.close)
        self.titlebar.bind("<ButtonPress-1>", self.dragging)
        self.titlebar.bind("<B1-Motion>", self.moving)
        self.titlebar.bind("<Double-Button-1>", self.maxsize)
        self.titlebar.bind("<Button-3>", self.popupmenu)
        self.setup()

        self.icon.pack(fill=Y, side=LEFT, padx=5, pady=5)
        self.text.pack(fill=Y, side=LEFT, pady=5)
        self.exit.pack(fill=Y, side=RIGHT)
        self.max.pack(fill=Y, side=RIGHT)
        self.min.pack(fill=Y, side=RIGHT)
        self.titlebar.pack(fill=X, side=TOP)
        self.titlebar.pack_propagate(0)

    # Titlebar
    def titlebarconfig(self, color: dict[str]={"color": None, "color_nf": None}, height: int=30) -> None:
        """Config for titlebar"""
        if color["color"] and color["color_nf"]:  # Require two colors : focuson & focusout
            self.bg = color["color"]
            self.nf = color["color_nf"]
            self["background"] = color["color"]

        if self.unlimit:
            self.titlebar["height"] = height
        else:
            if height > 30 and height <= 50:
                self.titlebar["height"] = height

        self.focusout()
        self.focusin()
        self.update()

    # Titlename
    # TODO: improve it
    def title(self, text: str) -> None:
        """Rebuild tkinter's title"""
        # TODO: show "..." if title is too long
        self.text["text"] = text
        self.wm_title(text)

    def title_grey(self) -> None:
        """..."""
        self.text["foreground"] = "grey"

    def title_back(self) -> None:
        """..."""
        self.text["foreground"] = "white"

    def usetitle(self, flag: bool=True)  -> None:
        """Show / forget titlename"""
        if not flag:
            self.text.pack_forget()

    def titleconfig(self, pack: str="left", font:str =None) -> None:
        """Config the title"""
        self.usetitle(False)
        if pack == "left":
            self.text.pack(side=LEFT)
        elif pack == "right":
            self.text.pack(side=RIGHT)
        else:
            self.text.config(justify="center")
            self.text.pack(expand=True)
        if font:
            self.text.config(font=font)

    # Titleicon
    def useicon(self, flag: bool = True) -> None:
        """Show / forget icon"""
        if not flag:
            self.icon.pack_forget()

    def popupmenu(self, event: Event) -> None:
        """Popup menu"""
        self.popup.post(event.x_root, event.y_root)

    def loadimage(self, image: str) -> None:
        """Load image"""
        self._icon = Image.open(image)
        self._icon = self._icon.resize((16, 16))
        self._img = ImageTk.PhotoImage(self._icon)
        self.icon["image"] = self._img

    def iconphoto(self, image: str) -> None:
        """Rebuild tkinter's iconphoto"""
        self.loadimage(image)
        self.wm_iconphoto(self._img)

    def iconbitmap(self, image: str) -> None:
        """Rebuild tkinter's iconbitmap"""
        self.loadimage(image)
        self.wm_iconbitmap(image)

    # Titlebutton
    # TODO: remove all of them
    def exit_grey(self, event=None):
        """..."""
        self.exit["image"] = self.close_img

    def exit_back(self, event=None):
        """..."""
        self.exit["image"] = self.close_hov_img

    def min_grey(self, event=None):
        """..."""
        self.min["image"] = self.min_img

    def min_back(self, event=None):
        """..."""
        self.min["image"] = self.min_hov_img

    def max_on_leave(self, event=None):
        """..."""
        self.max["background"] = self.bg

    # TODO: remove it
    def disabledo(self):
        """..."""
        pass
    
    # TODO: Combine it with titlebarconfig
    def usemaxmin(self, minsize=True, maxsize=True, minshow=True, maxshow=True):
        """Show / Disable min / max button"""
        if not minshow:
            self.min.pack_forget()
        elif not minsize:
            self.min_grey(None)
            self.min["command"] = self.disabledo
            self.min.unbind("<Leave>")
            self.min.unbind("<Enter>")

        if not maxshow:
            self.max.pack_forget()
        elif not maxsize:
            self.max_grey(None)
            self.max["command"] = self.disabledo
            self.max.unbind("<Leave>")
            self.max.unbind("<Enter>")

    # Window functions
    # TODO: rewrite it
    def setup(self):
        """Window Setup"""
        def handle(hwnd, msg, wp, lp):
            if msg == WM_NCCALCSIZE:
                sz = NCCALCSIZE_PARAMS.from_address(lp)
                sz.rgrc[0].top -= 6
            return windll.user32.CallWindowProcW(*map(c_uint64, (globals()[old], hwnd, msg, wp, lp)))

        self.title("CTT")
        self.geometry("%sx%s" % (self.width, self.height))
        self.iconbitmap(env / "asset" / "tk.ico")

        self.hwnd = windll.user32.FindWindowW(c_char_p(None), "CTT")
        plugin.setwindow(self.hwnd)

        limit_num = 200
        for i in range(limit_num):
            if "old_wndproc_%d" % i not in globals():
                old, new = "old_wndproc_%d"%i, "new_wndproc_%d"%i
                break

        prototype = WINFUNCTYPE(c_uint64, c_uint64, c_uint64, c_uint64, c_uint64)

        globals()[old] = None
        globals()[new] = prototype(handle)

        globals()[old] = windll.user32.GetWindowLongPtrA(self.hwnd, GWL_WNDPROC)
        windll.user32.SetWindowLongPtrA(self.hwnd, GWL_WNDPROC, globals()[new])

        self.update()
        self.focus_force()

    def dragging(self, event: Event) -> None:
        """Drag the window"""
        global x, y
        x = event.x
        y = event.y

    # TODO: rewrite it with ctypes
    def moving(self, event: Event) -> None:
        """Move the window"""
        global x, y
        if not self.fullscreen:
            plugin.move(self.hwnd, self.winfo_x(), self.winfo_y(), event.x - x, event.y - y)  # Use C for speed
        else:
            self.resize()

    # TODO: rewrite the maxsize function
    def maxsize(self, event: Event | None = None) -> None:
        """Maxsize Window"""
        if event and self.fullscreen:
            self.resize()
        else:
            geometry = self.wm_geometry().split("+")[0].split("x")
            self.width, self.height = geometry[0], geometry[1]
            self.popup.entryconfig("Restore", state="active")
            self.popup.entryconfig("Maxsize", state="disabled")
            self.w_x, self.w_y = self.winfo_x(), self.winfo_y()
            self.fullscreen = True
            self.max["image"] = self.max_hov_img
            self.max["command"] = self.resize
            w, h = self.wm_maxsize()
            self.geometry("%dx%d-1+0" % (w - 14, h - 40))

    def resize(self) -> None:
        """Resize window"""
        self.popup.entryconfig("Restore", state="disabled")
        self.popup.entryconfig("Maxsize", state="active")
        self.wm_geometry("%dx%d+%d+%d" % (int(self.width), int(self.height), int(self.w_x), int(self.w_y)))
        self.max["command"] = self.maxsize
        self.max["image"] = self.full_hov_img
        self.fullscreen = False

    def minsize(self) -> None:
        """Minsize window"""
        self.attributes("-alpha", 0)
        self.bind("<FocusIn>", self.deminsize)

    def deminsize(self, _: Event) -> None:
        """Deminsize window"""
        self.attributes("-alpha", 1)
        self.focusin()
        self.bind("<FocusIn>", self.focusin)

    # TODO: rewrite the setcolor function
    def setcolor(self, status: str, color: str) -> None:
        """Set the color"""
        if status == "out":
            self.exit_grey()
            self.min_grey()
            self.max_grey()
            self.title_grey()
            self.focus = True
        else:
            self.exit_back()
            self.min_back()
            self.max_back()
            self.title_back()
            self.focus = False

            if self.theme == "followsystem" or self.theme == "light":
                self.text["fg"] = self.colors[self.fg]

        self.titlebar["bg"] = color
        self.text["bg"] = color
        self.icon["bg"] = color
        self.min["bg"] = color
        self.max["bg"] = color
        self.exit["bg"] = color

    def focusout(self, _: Event) -> None:
        """When focusout"""
        self.setcolor("out", self.nf)

    def focusin(self, _: Event) -> None:
        """When focusin"""
        self.setcolor("in", self.bg)

    def close(self, _: Event) -> None:
        """Close Window"""
        self.destroy()

    # TODO: remove the function
    def sg(self, w: int, h: int) -> None:
        """Change the self.w and self.h"""
        self.width, self.height = w, h
        self.geometry("%sx%s" % (self.width, self.height))

    def geometry(self, size: str) -> None:
        """Rebuild tkinter's geometry"""
        if self.width and self.height:
            pass
        else:
            self.width, self.height = size.split("x")[0], size.split("x")[1]
        self.wm_geometry(size)

    def settheme(self, theme: str) -> None:
        """Set the window's theme"""
        self.theme = theme
        self.bg = self.colors[theme]
        self.nf = self.colors["%s_nf" % theme]
        self.fg = "light" if theme == "dark" else "dark"
        self.config(background=self.colors["%s_bg" % theme])
        self.update()

CTT().mainloop()