from pathlib import Path
from ctypes import byref, c_char_p, c_int, sizeof, windll
from tkinter import FLAT, LEFT, RIGHT, TOP, Button, Frame, Label, Menu, Tk, X, Y

from darkdetect import isDark
from PIL import Image, ImageTk

env = Path(__file__).parent
try: # Use ctype.windll.user32 someday
    plugin = windll.LoadLibrary(str(env / "plugin64.dll"))
except OSError:  # 32 bit
    plugin = windll.LoadLibrary(str(env / "plugin32.dll"))

color = {
    "light": "#ffffff", # Light normal
    "light_nf": "#f2efef", # Light not focus
    "dark": "#000000", # Dark normal
    "dark_nf": "#2b2b2b", # Dark not focus
    "dark_bg": "#202020", # Dark background
    "dark_afg": "#1a1a1a", # Dark active foreground
    "light_afg": "#e5e5e5", # Light active foreground
    "lighte_bg": "#f1707a",  # Light exit background
    "darke_bg": "#8b0a14", # Dark exit foreground
    "exit_fg": "#e81123", # Exit button foreground
}

class CTT(Tk):
    """Custom Tkinter Titlebar"""

    def __init__(self, theme: str):
        """Class initailser"""
        super().__init__()

        self.path = env / "asset"

        if theme == "auto":
            if isDark(): self.path /= "dark" else self.path /= "light"
            self.settheme(if isDark(): "dark" else "light")
        else:
            self.path /= theme
            self.settheme(theme)

        self.close_img = ImageTk.PhotoImage(Image.open(path / "close_50.png"))
        self.min_img = ImageTk.PhotoImage(Image.open(path / "minisize_50.png"))
        self.full_img = ImageTk.PhotoImage(Image.open(path / "fullwin_50.png"))
        self.max_img = ImageTk.PhotoImage(Image.open(path / "togglefull_50.png"))
        self.close_hov_img = ImageTk.PhotoImage(Image.open(path / "close_100.png"))
        self.min_hov_img = ImageTk.PhotoImage(Image.open(path / "minisize_100.png"))
        self.full_hov_img = ImageTk.PhotoImage(Image.open(path / "fullwin_100.png"))
        self.max_hov_img = ImageTk.PhotoImage(Image.open(path / "togglefull_100.png"))

        self.width, self.height = 265, 32-
        
        self.menu = Menu(self, tearoff=0) # TODO: improve the menu
        self.menu.add_command(label="Restore", command=self.resize)
        self.menu.add_command(label="Minsize", command=self.minsize)
        self.menu.add_command(label="Maxsize", command=self.maxsize)
        self.menu.add_separator()
        self.menu.add_command(label="Close (Alt+F4)", command=self.destroy)
        self.menu.entryconfig("Restore", state="disabled")


    def settheme(self, theme: str) -> None:
        """Set the window's theme"""
        self.theme = theme
        self.bg = colors["%s" % theme]
        self.nf = colors["%s_nf" % theme]
        self.fg = if theme == "dark": "light" else "dark"
        self.config(background=colors["%s_bg"] % theme)

        self.update()
