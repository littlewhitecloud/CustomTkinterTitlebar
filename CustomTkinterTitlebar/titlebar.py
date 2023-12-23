"""A special window for custom titlebar"""
from ctypes import WINFUNCTYPE, c_char_p, c_uint64, windll
from pathlib import Path
from tkinter import FLAT, LEFT, RIGHT, TOP, Button, Event, Frame, Label, Menu, Tk, X, Y

from darkdetect import isDark
from data import *
from PIL import Image, ImageTk

env = Path(__file__).parent


class CTT(Tk):
    """Custom Tkinter Titlebar Window Class"""

    def __init__(self, theme: str = "auto", unlimit: bool = False):
        """Class initialiser"""
        super().__init__()

        self.colors = {
            "light": "#ffffff",
            "light_nf": "#f2efef",
            "dark": "#202020",
            "dark_nf": "#797979",
            "dark_bg": "#262626",
            "button_dark_activefg": "#2D2D2D",
            "button_light_activefg": "#e5e5e5",
            "lightexit_bg": "#f1707a",
            "darkexit_bg": "#C42B1C",
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
        self.min = Button(self.titlebar, bg=self.bg, bd=0, width=44, relief=FLAT)
        self.max = Button(self.titlebar, bg=self.bg, bd=0, width=44, relief=FLAT)
        self.exit = Button(self.titlebar, bg=self.bg, bd=0, width=44, relief=FLAT)

        self.exit.config(
            activebackground=self.colors[f"{self.theme}exit_bg"],
            image=self.close_hov_img,
            command=self.quit,
        )
        self.min.config(
            activebackground=self.colors[f"button_{self.theme}_activefg"],
            image=self.min_hov_img,
            command=self.minsize,
        )
        self.max.config(
            activebackground=self.colors[f"button_{self.theme}_activefg"],
            image=self.full_hov_img,
            command=self.maxsize,
        )

        self.bind("<FocusOut>", self.focusout)
        self.bind("<FocusIn>", self.focusin)

        self.exit.bind("<Enter>", lambda _: self.exit.config(background=self.colors["exit_fg"]))
        self.exit.bind("<Leave>", lambda _: self.exit.config(background=self.nf if self.focus else self.bg))

        self.max.bind("<Enter>", lambda _: self.max.config(image=self.full_img if self.fullscreen else self.max_img))
        self.max.bind("<Leave>", lambda _: self.max(image=self.full_hov_img if self.fullscreen else self.max_hov_img))
        self.min.bind("<Enter>", lambda _: self.min.config(background=self.colors[f"button_{self.theme}_activefg"]))
        self.min.bind("<Leave>", lambda _: self.min.config(background=self.bg))
        self.max.bind("<Enter>", lambda _: self.max.config(background=self.colors[f"button_{self.theme}_activefg"]))
        self.max.bind("<Leave>", lambda _: self.max.config(background=self.bg))

        self.icon.bind("<Button-1>", lambda event: self.popup.post(event.x_root, event.y_root))
        self.titlebar.bind("<ButtonPress-1>", self.dragging)
        self.titlebar.bind("<B1-Motion>", self.moving)
        self.titlebar.bind("<Double-Button-1>", self.maxsize)
        self.titlebar.bind("<Button-3>", lambda event: self.popup.post(event.x_root, event.y_root))
        self.setup()

        self.icon.pack(fill=Y, side=LEFT, padx=5, pady=5)
        self.text.pack(fill=Y, side=LEFT, pady=5)
        self.exit.pack(fill=Y, side=RIGHT)
        self.max.pack(fill=Y, side=RIGHT)
        self.min.pack(fill=Y, side=RIGHT)
        self.titlebar.pack(fill=X, side=TOP)
        self.titlebar.pack_propagate(0)

    # Window
    def setup(self) -> None:
        """Window Setup"""

        def handle(hwnd: any, msg: any, wp: any, lp: any) -> any:
            if msg == WM_NCCALCSIZE:
                sz = NCCALCSIZE_PARAMS.from_address(lp)
                sz.rgrc[0].top -= 6

            return windll.user32.CallWindowProcW(*map(c_uint64, (globals()[old], hwnd, msg, wp, lp)))

        self.title("CTT")
        self.geometry(f"{self.width}x{self.height}")
        self.iconbitmap(env / "asset" / "tk.ico")
        self.hwnd = windll.user32.FindWindowW(c_char_p(None), "CTT")

        windll.user32.SetWindowLongA(self.hwnd, GWL_EXSTYLE, WS_EX_APPWINDOW)
        windll.user32.SetWindowLongA(self.hwnd, GWL_STYLE, WS_VISIBLE | WS_THICKFRAME)

        old, new = "old", "new"
        prototype = WINFUNCTYPE(c_uint64, c_uint64, c_uint64, c_uint64, c_uint64)
        globals()[old] = None
        globals()[new] = prototype(handle)
        globals()[old] = windll.user32.GetWindowLongPtrA(self.hwnd, GWL_WNDPROC)
        windll.user32.SetWindowLongPtrA(self.hwnd, GWL_WNDPROC, globals()[new])

    def settheme(self, theme: str) -> None:
        """Config the theme"""
        self.theme = theme
        self.bg = self.colors[theme]
        self.nf = self.colors[f"{theme}_nf"]
        self.fg = "light" if theme == "dark" else "dark"
        self.config(background=self.colors[f"{theme}_bg"])
        self.update()

    def dragging(self, event: Event) -> None:
        """Drag the window"""
        global x, y
        x = event.x
        y = event.y

    def moving(self, event: Event) -> None:
        """Move the window"""
        global x, y
        if not self.fullscreen:
            windll.user32.SetWindowPos(
                self.hwnd,
                None,
                event.x - x + self.winfo_x(),
                event.y - y + self.winfo_y(),
                0,
                0,
                SWP_NOREDRAW | SWP_NOSIZE | SWP_FRAMECHANGED,
            )
        else:
            self.resize()

    # Titlebar
    def titlebarconfig(
        self,
        useicon: bool = True,
        usetitle: bool = True,
        titlepack: str | None = None,
        font: tuple | None = None,
        titlecolor: str | None = None,
        usemin: bool = True,
        usemax: bool = True,
        disablemin: bool = False,
        disablemax: bool = False,
        color: dict[str] = {"color": None, "color_nf": None},
        height: int = 30,
    ) -> None:
        """Config he titlebar"""
        if not useicon:
            self.icon.pack_forget()

        if not usetitle:
            self.text.pack_forget()
        elif titlepack:
            self.text.pack_forget()
            self.text.pack(titlepack)
        elif font:
            self.text.config(font=font)
        elif color:
            self.text.config(foreground=titlecolor)

        if not usemin:
            self.min.pack_forget()
        if not usemax:
            self.max.pack_forget()

        if not disablemin:
            self.min.config(command=lambda: ..., image=self.min_img)
            self.min.unbind("<Leave>")
            self.min.unbind("<Enter>")

        if not disablemax:
            self.max.config(command=lambda: ..., image=self.full_img)
            self.max.unbind("<Leave>")
            self.max.unbind("<Enter>")

        if color["color"] and color["color_nf"]:
            self.bg = color["color"]
            self.nf = color["color_nf"]

        if height != 30:
            self.titlebar["height"] = height

        self.withdraw()
        self.deiconify()

    # Functions
    def title(self, text: str) -> None:
        """Rebuild tkinter's title"""
        # TODO: show "..." if title is too long
        self.text.config(text=text)
        self.wm_title(text)

    def iconphoto(self, image: str) -> None:
        """Rebuild tkinter's iconphoto"""
        self.img = ImageTk.PhotoImage(Image.open(image).resize((16, 16)))
        self.icon.config(image=self.img)
        self.wm_iconphoto(self._img)

    def iconbitmap(self, image: str) -> None:
        """Rebuild tkinter's iconbitmap"""
        self.img = ImageTk.PhotoImage(Image.open(image).resize((16, 16)))
        self.icon.config(image=self.img)
        self.wm_iconbitmap(image)

    def geometry(self, size: str) -> None:
        """Rebuild tkinter's geometry"""
        self.width, self.height = size.split("x")[0], size.split("x")[1]
        self.wm_geometry(size)

    # Titlebutton
    # TODO: remove all of them
    def title_grey(self) -> None:
        """..."""
        self.text["foreground"] = "grey"

    def title_back(self) -> None:
        """..."""
        self.text["foreground"] = "white"

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
        self.fullscreen = False
        self.popup.entryconfig("Restore", state="disabled")
        self.popup.entryconfig("Maxsize", state="active")
        self.wm_geometry("%dx%d+%d+%d" % (int(self.width), int(self.height), int(self.w_x), int(self.w_y)))
        self.max.config(image=self.full_hov_img, command=self.maxsize)

    # TODO: minsize the window with win32 functions
    def minsize(self) -> None:
        """Minsize window"""
        self.attributes("-alpha", 0)
        self.bind("<FocusIn>", self.deminsize)

    # TODO: see above
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
            self.max.config(image=self.full_img)
            self.title_grey()
            self.focus = True
        else:
            self.exit_back()
            self.min_back()
            self.max.config(image=self.full_hov_img)
            self.title_back()
            self.focus = False

            if self.theme == "followsystem" or self.theme == "light":
                self.text["fg"] = self.colors[self.fg]

    def focusout(self, _: Event | None = None) -> None:
        """When focusout"""
        self.setcolor("out", self.nf)

    def focusin(self, _: Event | None = None) -> None:
        """When focusin"""
        self.setcolor("in", self.bg)
        # TODO: unbind the three button's leave enter


if __name__ == "__main__":
    CTT().mainloop()
