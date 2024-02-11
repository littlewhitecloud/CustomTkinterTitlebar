"""A special window for custom titlebar"""

from ctypes import WINFUNCTYPE, c_char_p, c_uint64, windll
from pathlib import Path
from tkinter import Button, Event, Frame, Label, Menu, Tk
from typing import Any, Mapping

from darkdetect import isDark
from data import *
from PIL import Image, ImageTk

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

        self.width, self.height = 265, 320
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
        self.min = Button(self.titlebar, bg=self.bg, bd=0, width=44, relief="flat")
        self.max = Button(self.titlebar, bg=self.bg, bd=0, width=44, relief="flat")
        self.exit = Button(self.titlebar, bg=self.bg, bd=0, width=44, relief="flat")

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
        self.exit.bind("<Leave>", lambda _: self.exit.config(background=self.bg))

        self.max.bind("<Enter>", lambda _: self.max.config(image=self.full_img if self.fullscreen else self.max_img))
        self.max.bind("<Leave>", lambda _: self.max.config(image=self.full_hov_img if self.fullscreen else self.max_hov_img))
        self.min.bind("<Enter>", lambda _: self.min.config(background=self.colors[f"button_{self.theme}_activefg"]))
        self.min.bind("<Leave>", lambda _: self.min.config(background=self.bg))
        self.max.bind("<Enter>", lambda _: self.max.config(background=self.colors[f"button_{self.theme}_activefg"]))
        self.max.bind("<Leave>", lambda _: self.max.config(background=self.bg))

        self.icon.bind("<Button-1>", lambda event: self.popup.post(event.x_root, event.y_root))
        for widget in (self.titlebar, self.text):
            widget.bind("<ButtonPress-1>", self.dragging)
            widget.bind("<B1-Motion>", self.moving)

        self.titlebar.bind("<Double-Button-1>", self.maxsize)
        self.titlebar.bind("<Button-3>", lambda event: self.popup.post(event.x_root, event.y_root))

        self.setup()

        self.icon.pack(fill="y", side="left", padx=5, pady=5)
        self.text.pack(fill="y", side="left", pady=5)
        self.exit.pack(fill="y", side="right")
        self.max.pack(fill="y", side="right")
        self.min.pack(fill="y", side="right")
        self.titlebar.pack(fill="x", side="top")
        self.titlebar.pack_propagate(False)

    # Window
    def setup(self) -> None:
        """Window Setup"""

        def handle(hwnd: int, msg: int, wp: int, lp: int) -> int:
            if msg == WM_NCCALCSIZE and wp:
                sz = NCCALCSIZE_PARAMS.from_address(lp)
                sz.rgrc[0].top -= 6

            return windll.user32.CallWindowProcW(*map(c_uint64, (globals()[old], hwnd, msg, wp, lp)))

        self.title("CTT")
        self.geometry(f"{self.width}x{self.height}")
        self.iconbitmap(str(env / "asset" / "tk.ico"))

        self.hwnd = windll.user32.FindWindowW(c_char_p(None), "CTT")

        windll.user32.SetWindowLongA(self.hwnd, GWL_EXSTYLE, WS_EX_APPWINDOW)
        windll.user32.SetWindowLongA(self.hwnd, GWL_STYLE, WS_VISIBLE | WS_THICKFRAME)

        old, new = "old", "new"
        prototype = WINFUNCTYPE(c_uint64, c_uint64, c_uint64, c_uint64, c_uint64)
        globals()[old] = None
        globals()[new] = prototype(handle)
        globals()[old] = windll.user32.GetWindowLongPtrA(self.hwnd, GWL_WNDPROC)
        windll.user32.SetWindowLongPtrA(self.hwnd, GWL_WNDPROC, globals()[new])

        self.update()
        self.focus_force()

    def settheme(self, theme: str) -> None:
        """Config the theme"""

        def autotheme() -> str:
            return "dark" if isDark() else "light"

        self.theme = theme
        if theme not in ("dark", "light", "auto"):  # Check the theme
            print(f"Warning: Now the theme is `{theme}`, not matching `D(d)ark` `L(l)ight` `A(a)uto`, using auto mode instead")
            self.theme = autotheme()
        elif theme == "auto":
            self.theme = autotheme()

        self.bg = self.colors[self.theme]
        self.nf = self.colors[f"{self.theme}_nf"]
        self.fg = "light" if self.theme == "dark" else "dark"
        self.config(background=self.colors[f"{self.theme}_bg"])
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

        self.usemax = usemax and not disablemax
        self.usemin = usemin and not disablemin

        if not usemin:
            self.min.pack_forget()
        if not usemax:
            self.max.pack_forget()

        if disablemin:
            self.min.config(command=lambda: ..., image=self.min_img)
            self.min.unbind("<Leave>")
            self.min.unbind("<Enter>")

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
            self.titlebar["height"] = height

        self.update_idletasks()
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

    # TODO: parse  %sx%s+%s+%s
    def geometry(self, size: str) -> None:
        """Rebuild tkinter's geometry"""
        self.width, self.height = size.split("x")[0], size.split("x")[1]
        self.wm_geometry(size)

    def maxsize(self, _: None = None) -> None:
        """Maxsize Window"""
        self.fullscreen = True

        self.popup.entryconfig("Restore", state="active")
        self.popup.entryconfig("Maxsize", state="disabled")

        self.max.config(image=self.max_hov_img, command=self.resize)

        windll.user32.ShowWindow(self.hwnd, SW_MAXIMIZE)
        # TODO: leave a place for the taskbar

    def resize(self, _: None = None) -> None:
        """Resize window"""
        self.fullscreen = False
        self.popup.entryconfig("Restore", state="disabled")
        self.popup.entryconfig("Maxsize", state="active")
        self.max.config(image=self.full_hov_img, command=self.maxsize)

        windll.user32.ShowWindow(self.hwnd, SW_NORMAL)

    def minsize(self) -> None:
        """Minsize window"""
        windll.user32.SetWindowLongW(self.hwnd, GWL_STYLE, WS_VISIBLE | WS_THICKFRAME | WS_CAPTION)  # for the animation
        windll.user32.SendMessageW(self.hwnd, WM_SYSCOMMAND, SC_MINIMIZE, 0)

    def setcolor(self) -> None:
        """Set the color"""

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

        if self.theme == "light" and self.onfocus:  # TODO: ???
            self.text["fg"] = self.colors[self.fg]

    def focusout(self, _: Event | None = None) -> None:
        """When focusout"""
        self.onfocus = False
        self.setcolor(self.nf)

    def focusin(self, _: Event | None = None) -> None:
        """When focusin"""
        self.onfocus = True
        self.setcolor(self.bg)
        # TODO: unbind the three button's leave enter
        windll.user32.SetWindowLongW(self.hwnd, GWL_STYLE, WS_VISIBLE | WS_THICKFRAME)  # for the animation


if __name__ == "__main__":
    test = CTT()
    test.mainloop()
