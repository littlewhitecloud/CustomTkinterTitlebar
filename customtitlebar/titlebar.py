"""A special window for custom titlebar"""

from __future__ import annotations

import pathlib
from ctypes import WINFUNCTYPE, c_uint64, windll
from platform import win32_ver
from tkinter import Button, Event, Frame, Label, Tk
from typing import Any, Dict, Literal, Mapping, Optional, Tuple

import darkdetect
from PIL import Image, ImageTk

from .data import *

__all__ = ["CTT"]

class CTT(Tk):
    """Customize window for customize titlebar"""

    def __init__(self, theme: Literal["light", "dark", "auto"] = "auto") -> None:
        """
        * `theme`: the theme of the window ("light", "dark", "auto")
        """
        super().__init__()

        self.colors = {
            "light": "#fafafa",
            "light_nf": "#f3f3f3",
            "dark": "#202020",
            "dark_nf": "#797979",
            "dark_activefg": "#2d2d2d",
            "light_activefg": "#e5e5e5",
            "lightexit_bg": "#f1707a",
            "darkexit_bg": "#c42b1c",
            "exit_fg": "#e81123",
        }

        self.width, self.height = 200, 230
        self.snaplayout = self.fullscreen = False
        self.onfocus = self.usemax = self.usemin = True
        self.path = pathlib.Path(__file__).parent / "asset"
        self.titlebarheight = 0

        self.gettheme(theme.lower())
        self.assetpath = self.path / self.theme
        self.settheme(self.theme)

        self.close_img = ImageTk.PhotoImage(Image.open(self.assetpath / "close_50.png"))
        self.min_img = ImageTk.PhotoImage(Image.open(self.assetpath / "minisize_50.png"))
        self.full_img = ImageTk.PhotoImage(Image.open(self.assetpath / "fullwin_50.png"))
        self.max_img = ImageTk.PhotoImage(Image.open(self.assetpath / "togglefull_50.png"))
        self.close_hov_img = ImageTk.PhotoImage(Image.open(self.assetpath / "close_100.png"))
        self.min_hov_img = ImageTk.PhotoImage(Image.open(self.assetpath / "minisize_100.png"))
        self.full_hov_img = ImageTk.PhotoImage(Image.open(self.assetpath / "fullwin_100.png"))
        self.max_hov_img = ImageTk.PhotoImage(Image.open(self.assetpath / "togglefull_100.png"))

        self.titlebar = Frame(self, height=30)
        self.buttongroup = Frame(self.titlebar)
        self.infogroup = Frame(self.titlebar)
        self.icon = Label(self.infogroup)
        self.text = Label(self.infogroup, fg=self.colors[self.fg])

        self.min = Button(self.buttongroup, command=self.iconify)
        self.max = Button(self.buttongroup, command=self.maximize)
        self.exit = Button(self.buttongroup, command=self.quit)

        for _ in (self.min, self.max, self.exit):
            _.config(bd=0, width=44, height=30, relief="flat")

        self.bind("<FocusOut>", lambda _: self.setimage(False))
        self.bind("<FocusIn>", lambda _: self.setimage(True))

        self.exit.bind("<Enter>", lambda _: self.exit.config(background=self.colors["exit_fg"]))
        self.exit.bind("<Leave>", lambda _: self.exit.config(background=self.bg))

        self.min.bind("<Enter>", lambda _: self.min.config(background=self.ag))
        self.min.bind("<Leave>", lambda _: self.min.config(background=self.bg))

        self.max.bind("<Enter>", lambda _: self.maximize_enter())
        self.max.bind("<Leave>", lambda _: self.maximize_leave())

        for _ in (self.titlebar, self.text):
            _.bind("<B1-Motion>", self.moving)

        self.titlebar.bind("<Double-Button-1>", self.maximize)

        self.icon.pack(fill="x", side="left")
        self.text.pack(fill="x", side="left")
        for _ in (self.exit, self.max, self.min):
            _.pack(fill="y", side="right")
        self.infogroup.pack(fill="x", side="left", padx=5, pady=5)
        self.buttongroup.pack(fill="y", side="right")

        self.titlebar.pack(fill="x", side="top", expand=False)
        self.titlebar.pack_propagate(False)

        self.title("Tk")
        self.minsize(self.width, self.height)
        self.iconbitmap(str(self.path / "tk.ico"))
        self.setcolor()
        self.setimage(True)

        self.get_window_titlebar_height()

        self.setup()

    # Window
    def setup(self) -> None:
        """Setup the window"""

        def WndProc(hwnd: Any, msg: Any, wp: Any, lp: Any) -> Any:
            """Handle message"""
            if msg == WM_NCCALCSIZE and wp:
                lpncsp = NCCALCSIZE_PARAMS.from_address(lp)
                lpncsp.rgrc[0].top -= self.titlebarheight

            return windll.user32.CallWindowProcW(*map(c_uint64, (globals()[old], hwnd, msg, wp, lp)))

        self.hwnd = windll.user32.GetParent(self.winfo_id())

        old, new = "old", "new"
        prototype = WINFUNCTYPE(c_uint64, c_uint64, c_uint64, c_uint64, c_uint64)

        globals()[old] = None
        globals()[new] = prototype(WndProc)
        globals()[old] = windll.user32.GetWindowLongPtrA(self.hwnd, GWL_WNDPROC)
        windll.user32.SetWindowLongPtrW(self.hwnd, GWL_WNDPROC, globals()[new])

        windll.user32.SetWindowPos(self.hwnd, None, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE | SWP_FRAMECHANGED)

    def moving(self, event: Event) -> None:
        """Move window"""
        if self.fullscreen:
            self.resize(event)

        windll.user32.ReleaseCapture()
        windll.user32.SendMessageA(self.hwnd, WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0)

    # Maximize
    def maximize(self, _: Optional[Event] = None) -> None:
        """Maximize Window"""
        self.fullscreen = True

        self.max.config(image=self.max_hov_img, command=self.resize)
        self.titlebar.bind("<Double-Button-1>", self.resize)

        windll.user32.ShowWindow(self.hwnd, SW_MAXIMIZE)

    def maximize_enter(self) -> None:
        """..."""
        self.max.config(background=self.ag)

        if self.snaplayout:
            return

        self.snaplayout = True
        self.after(1000, self.call_snaplayout)

    def maximize_leave(self) -> None:
        """..."""
        self.max.config(background=self.bg)
        self.snaplayout = False

    def resize(self, _: Optional[Event] = None) -> None:
        """Resize window"""
        self.fullscreen = False

        self.max.config(image=self.full_hov_img, command=self.maximize)
        self.titlebar.bind("<Double-Button-1>", self.maximize)

        windll.user32.ShowWindow(self.hwnd, SW_NORMAL, 0, 0)

    def call_snaplayout(self) -> None:
        """..."""
        if not self.snaplayout:
            return

        # TODO: improve the way to call snap layout
        windll.user32.keybd_event(91, 0, 0, 0)
        windll.user32.keybd_event(90, 0, 0, 0)
        windll.user32.keybd_event(91, 0, 2, 0)
        windll.user32.keybd_event(90, 0, 2, 0)
        self.snaplayout = False

    # Titlebar
    def titlebarconfig(
        self,
        usemin: bool = True,
        usemax: bool = True,
        disablemin: bool = False,
        disablemax: bool = False,
        useicon: bool = True,
        usetitle: bool = True,
        font: Optional[Tuple] = None,
        height: Optional[int] = None,
        titlecolor: Optional[str] = None,
        titlepack: Optional[Mapping[str, Any]] = None,
        color: Dict[str, Any] = {"color": None, "color_nf": None},
    ) -> None:
        """
        Config titlebar
        * `height`: Config the height of the titlebar
        * `usemin`: Flag to enable to use the minimize button
        * `usemax`: Flag to enable to usethe maximize button
        * `disablemin`: Flag to enable the minimize button
        * `disablemax`: Flag to enable the maximize button
        * `useicon`: Flag to enable to show the icon in the titlebar
        * `usetitle`: Flag to enable to show the text in the titlebar
        * `font`: Set the font of the text
        * `titlepack`: Config the pack of the text
        * `titlecolor`: Config the color of the text
        * `color`: Config the color of the titlebar
        """
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

            for _ in (self.titlebar, self.text, self.icon, self.min, self.max, self.exit):
                _.config(background=self.bg)

        if height:
            self.titlebar.config(height=height)

        if not (useicon and usetitle):
            self.infogroup.pack_forget()

        self.update_idletasks()

    # Original Tkinter functions
    def title(self, text: Optional[str] = None) -> None:
        """tkinter's title"""
        # TODO: show "..." if title is too long

        if not text:
            return self.text["text"]

        self.text.config(text=text)
        self.wm_title(text)

    def iconphoto(self, image: Optional[str] = None) -> None:
        """tkinter's iconphoto"""
        if not image:
            return

        self.img = ImageTk.PhotoImage(Image.open(image).resize((16, 16)))
        self.icon.config(image=self.img)
        self.wm_iconphoto(self.img)

    def iconbitmap(self, image: Optional[str] = None) -> None:
        """tkinter's iconbitmap"""
        if not image:
            return

        self.img = ImageTk.PhotoImage(Image.open(image).resize((16, 16)))
        self.icon.config(image=self.img)
        self.wm_iconbitmap(image)

    def geometry(self, size: Optional[str] = None) -> None:
        """tkinter's geometry"""
        if not size:
            return self.wm_geometry()

        _ = size.split("+")[0].split("x")
        self.width, self.height = _[0], _[1]

        self.wm_geometry(size)

    # Theme
    def gettheme(self, theme: Literal["light", "dark", "auto"] = "auto") -> None:
        "Get theme"
        if theme.lower() in ("light", "dark"):
            self.theme = theme
        else:
            self.theme = darkdetect.theme()  # ignore typo and other situation ...
        self.theme = self.theme.lower()

    def settheme(self, theme: Optional[Literal["light", "dark", "auto"]] = None) -> None:
        """Config theme"""
        if not theme:
            self.gettheme()
        else:
            self.theme = theme

        self.assetpath = self.path / self.theme  # type: ignore

        self.bg = self.colors[f"{self.theme}"]
        self.nf = self.colors[f"{self.theme}_nf"]
        self.ag = self.colors[f"{self.theme}_activefg"]
        self.fg = "light" if self.theme == "dark" else "dark"

        # TODO: figure out why
        try:
            self.setcolor()
        except:
            pass

        self.update_idletasks()

    def setcolor(self) -> None:
        """Set the color of the widgets"""
        for _ in (
            self,
            self.titlebar,
            self.buttongroup,
            self.infogroup,
            self.icon,
            self.text,
            self.min,
            self.max,
            self.exit,
        ):
            _.config(background=self.bg)
        for _ in (self.min, self.max):
            _.config(activebackground=self.ag)

        self.exit.config(activebackground=self.colors[f"{self.theme}exit_bg"])

        self.update_idletasks()

    def setimage(self, focus: bool) -> None:
        """Set the image of the widgets"""

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

        # Also set the foreground of the title
        self.text.config(
            foreground=(
                "grey" if not self.onfocus else (self.colors[self.fg] if self.theme == "light" else self.colors[self.fg])
            )
        )

    def get_window_titlebar_height(self) -> None:
        """Get the correct titlebar hegiht via system version"""
        self.titlebarheight = self.winfo_rooty() - self.winfo_y() - (1 if "11" == win32_ver()[0] else 0)
