"""A special window for custom titlebar"""

from ctypes import WINFUNCTYPE, c_char_p, c_uint64, windll
from pathlib import Path
from tkinter import Button, Event, Frame, Label, Tk
from typing import Any, Mapping

from darkdetect import isDark
from PIL import Image, ImageTk

from .data import *
env = Path(__file__).parent


class CTT(Tk):
    """Custom Tkinter Titlebar Window Class"""

    def __init__(self, theme: str = "auto") -> None:
        super().__init__()
        self.colors = {
            "light": "#eeeeee",
            "light_nf": "#f2efef",
            "light_bg": "#eeeeee",
            "dark": "#202020",
            "dark_nf": "#797979",
            "dark_bg": "#202020",
            "button_dark_activefg": "#2D2D2D",
            "button_light_activefg": "#e5e5e5",
            "lightexit_bg": "#f1707a",
            "darkexit_bg": "#C42B1C",
            "exit_fg": "#e81123",
        }

        self.width, self.height = 1080, 607
        self.fullscreen = False
        self.onfocus = self.usemax = self.usemin = True

        self.settheme(theme.lower())
        self.path = env / "asset" / self.theme

        self.close_img = ImageTk.PhotoImage(Image.open(self.path / "close_50.png"))
        self.min_img = ImageTk.PhotoImage(Image.open(self.path / "minisize_50.png"))
        self.full_img = ImageTk.PhotoImage(Image.open(self.path / "fullwin_50.png"))
        self.max_img = ImageTk.PhotoImage(Image.open(self.path / "togglefull_50.png"))
        self.close_hov_img = ImageTk.PhotoImage(Image.open(self.path / "close_100.png"))
        self.min_hov_img = ImageTk.PhotoImage(Image.open(self.path / "minisize_100.png"))
        self.full_hov_img = ImageTk.PhotoImage(Image.open(self.path / "fullwin_100.png"))
        self.max_hov_img = ImageTk.PhotoImage(Image.open(self.path / "togglefull_100.png"))

        self.titlebar = Frame(self, bg=self.bg, height=30)
        self.buttongroup = Frame(self.titlebar, bg=self.bg)
        self.infogroup = Frame(self.titlebar, bg=self.bg)
        self.icon = Label(self.infogroup, bg=self.bg)
        self.text = Label(self.infogroup, bg=self.bg, fg=self.colors[self.fg])

        self.min = Button(self.buttongroup)
        self.max = Button(self.buttongroup)
        self.exit = Button(self.buttongroup)

        for widget in (self.min, self.max, self.exit):
            widget.config(bg=self.bg, bd=0, width=44, height=30, relief="flat")

        self.exit.config(
            activebackground=self.colors[f"{self.theme}exit_bg"],
            image=self.close_hov_img,
            command=self.quit,
        )
        self.min.config(
            activebackground=self.colors[f"button_{self.theme}_activefg"],
            image=self.min_hov_img,
            command=self.iconify,
        )
        self.max.config(
            activebackground=self.colors[f"button_{self.theme}_activefg"],
            image=self.full_hov_img,
            command=self.maximize,
        )

        self.bind("<FocusOut>", self.focusout)
        self.bind("<FocusIn>", self.focusin)

        self.exit.bind("<Enter>", lambda _: self.exit.config(background=self.colors["exit_fg"]))
        self.exit.bind("<Leave>", lambda _: self.exit.config(background=self.bg))

        self.max.bind("<Enter>", lambda _: self.max.config(image=self.full_img if self.fullscreen else self.max_img))
        self.max.bind("<Leave>", lambda _: self.max.config(image=self.full_hov_img if self.fullscreen else self.max_hov_img))
        self.min.bind("<Enter>", lambda _: self.min.config(background=self.colors[f"button_{self.theme}_activefg"]))
        self.min.bind("<Leave>", lambda _: self.min.config(background=self.bg))
        self.max.bind("<Enter>", lambda _: self.max.config(background=self.colors[f"button_{self.theme}_activefg"]))
        self.max.bind("<Leave>", lambda _: self.max.config(background=self.bg))

        for widget in (self.titlebar, self.text):
            widget.bind("<ButtonPress-1>", self.dragging)
            widget.bind("<B1-Motion>", self.moving)

        self.titlebar.bind("<Double-Button-1>", self.maximize)

        self.setup()

        self.icon.pack(fill="x", side="left")
        self.text.pack(fill="x", side="left")
        self.exit.pack(fill="y", side="right")
        self.max.pack(fill="y", side="right")
        self.min.pack(fill="y", side="right")
        self.infogroup.pack(fill = "x", side = "left", padx=5, pady=5)
        self.buttongroup.pack(fill = "y", side="right")
        self.titlebar.pack(fill="x", side="top", expand=False)
        self.titlebar.pack_propagate(False)

    # Window
    def setup(self) -> None:
        """Window Setup"""

        def handle(hwnd: int, msg: int, wp: int, lp: int) -> int:
            if msg == WM_NCCALCSIZE and wp:
                lpncsp = NCCALCSIZE_PARAMS.from_address(lp)
                lpncsp.rgrc[0].top -= 30

            return windll.user32.CallWindowProcW(*map(c_uint64, (globals()[old], hwnd, msg, wp, lp)))

        self.title("Tk")
        self.geometry(f"{self.width}x{self.height}")
        self.iconbitmap(str(env / "asset" / "tk.ico"))

        self.hwnd = windll.user32.FindWindowW(c_char_p(None), "Tk")

        old, new = "old", "new"
        prototype = WINFUNCTYPE(c_uint64, c_uint64, c_uint64, c_uint64, c_uint64)

        globals()[old] = None
        globals()[new] = prototype(handle)
        globals()[old] = windll.user32.GetWindowLongPtrA(self.hwnd, GWL_WNDPROC)
        windll.user32.SetWindowLongPtrA(self.hwnd, GWL_WNDPROC, globals()[new])

        self.update()

    def dragging(self, event: Event) -> None:
        """Drag the window"""
        self.x = event.x
        self.y = event.y

    def moving(self, event: Event) -> None:
        """Move the window"""
        if self.fullscreen:
            self.resize(event)

        windll.user32.SetWindowPos(
            self.hwnd,
            None,
            self.winfo_pointerx() - self.x,
            self.winfo_pointery() - self.y,
            0,
            0,
            SWP_NOREDRAW | SWP_NOSIZE | SWP_FRAMECHANGED,
        )

    def maximize(self, _: Event | None = None) -> None:
        """Maximize Window"""
        self.fullscreen = True

        self.max.config(image=self.max_hov_img, command=self.resize)
        self.titlebar.bind("<Double-Button-1>", self.resize)

        windll.user32.ShowWindow(self.hwnd, SW_MAXIMIZE)

    def resize(self, _: Event | None = None) -> None:
        """Resize window"""
        self.fullscreen = False
        self.max.config(image=self.full_hov_img, command=self.maximize)
        self.titlebar.bind("<Double-Button-1>", self.maximize)

        windll.user32.ShowWindow(self.hwnd, SW_NORMAL)

    # Titlebar
    def titlebarconfig(
        self,
        useicon: bool = True,
        usetitle: bool = True,
        titlepack: Mapping[str, Any] | None = None,
        font: tuple | None = None,
        titlecolor: str = "",
        usemin: bool = True,
        usemax: bool = True,
        disablemin: bool = False,
        disablemax: bool = False,
        color: dict = {"color": None, "color_nf": None},
        height: int = 30,
    ) -> None:
        """Config he titlebar"""
        if not useicon:
            self.icon.pack_forget()

        if not usetitle:
            self.text.pack_forget()
        if titlepack:
            self.text.pack_forget()
            self.text.pack(titlepack)
        if titlecolor:
            self.text.config(foreground=titlecolor)
        if font:
            self.text.config(font=font)
        if color:  # FIXME
            self.text.config(background=color["color"], foreground=color["color_nf"])

        self.usemin = usemin and not disablemin
        if not usemin:
            self.min.pack_forget()
        if disablemin:
            self.min.config(command=lambda: ..., image=self.min_img)
            self.min.unbind("<Leave>")
            self.min.unbind("<Enter>")

        self.usemax = usemax and not disablemax
        if not usemax:
            self.max.pack_forget()
        if disablemax:
            self.max.config(command=lambda: ..., image=self.full_img)
            self.max.unbind("<Leave>")
            self.max.unbind("<Enter>")

        if color["color"] and color["color_nf"]:
            self.bg = color["color"]
            self.nf = color["color_nf"]

            for widget in (self.titlebar, self.text, self.icon, self.min, self.max, self.exit):
                widget.config(background=self.bg)

        if height != 30:
            self.titlebar.config(height=height)

        self.update_idletasks()
        self.withdraw()
        self.deiconify()

    # Functions
    def title(self, text: str = "") -> None:
        """Rebuild tkinter's title"""
        # TODO: show "..." if title is too long

        if not text: return self.text["text"]

        self.text.config(text=text)
        self.wm_title(text)

    def iconphoto(self, image: str) -> None:
        """Rebuild tkinter's iconphoto"""
        self.img = ImageTk.PhotoImage(Image.open(image).resize((16, 16)))
        self.icon.config(image=self.img)
        self.wm_iconphoto(self.img)

    def iconbitmap(self, image: str) -> None:
        """Rebuild tkinter's iconbitmap"""
        self.wm_iconbitmap(image)

        if not image:
            return
        self.img = ImageTk.PhotoImage(Image.open(image).resize((16, 16)))
        self.icon.config(image=self.img)

    # TODO: parse  %sx%s+%s+%s
    def geometry(self, size: str) -> None:
        """Rebuild tkinter's geometry"""
        tmp = size.split('+')[0].split('x')
        self.width, self.height = tmp[0], tmp[1]

        self.wm_geometry(size)

    def settheme(self, theme: str) -> None:
        """Config the theme"""

        def autotheme() -> str:
            return "dark" if isDark() else "light"

        if theme not in ("dark", "light", "auto"):  # Check the theme
            print(
                f"Warning: Now the theme is `{theme}`, not matching `D(d)ark` `L(l)ight` `A(a)uto`, using auto mode instead"
            )
            self.theme = autotheme()

        if theme == "auto":
            self.theme = autotheme()
        else:
            self.theme = theme

        self.bg = self.colors[self.theme]
        self.nf = self.colors[f"{self.theme}_nf"]
        self.fg = "light" if self.theme == "dark" else "dark"
        self.config(background=self.colors[f"{self.theme}_bg"])
        self.update()

    def setcolor(self, focus: bool) -> None:
        """Set the color"""
        self.onfocus = focus
        self.exit.config(image=self.close_hov_img if self.onfocus else self.close_img)
        if self.usemin:
            self.min.config(image=self.min_hov_img if self.onfocus else self.min_img)
        if self.usemax:
            (
                self.max.config(image=self.max_hov_img if self.onfocus else self.max_img)
                if self.fullscreen
                else self.max.config(image=self.full_hov_img if self.onfocus else self.full_img)
            )
        self.text.config(foreground="white" if self.onfocus else "grey")

        if self.theme == "light" and self.onfocus:
            self.text.config(foreground=self.colors[self.fg])

    def focusout(self, _: Event | None = None) -> None: self.setcolor(False)
    def focusin(self, _: Event | None = None) -> None: self.setcolor(True)
