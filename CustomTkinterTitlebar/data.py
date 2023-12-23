from ctypes import POINTER, Structure, c_int
from ctypes.wintypes import HWND, RECT, UINT

WM_NCCALCSIZE = 0x0083
WS_EX_APPWINDOW = 0x00040000
WS_VISIBLE = 0x10000000
WS_THICKFRAME = 0x00040000

HTMAXBUTTON = 9

SWP_NOSIZE = 0x0001
SWP_NOREDRAW = 0x0008
SWP_FRAMECHANGED = 0x0020

GWL_EXSTYLE = -20
GWL_STYLE = -16
GWL_WNDPROC = -4


class PWINDOWPOS(Structure):
    _fields_ = [
        ("hWnd", HWND),
        ("hwndInsertAfter", HWND),
        ("x", c_int),
        ("y", c_int),
        ("cx", c_int),
        ("cy", c_int),
        ("flags", UINT),
    ]


class NCCALCSIZE_PARAMS(Structure):
    _fields_ = [("rgrc", RECT * 3), ("lppos", POINTER(PWINDOWPOS))]
