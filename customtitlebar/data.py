from ctypes import POINTER, Structure, c_int
from ctypes.wintypes import HWND, RECT, UINT

WM_NCCALCSIZE = 0x0083

SWP_NOSIZE = 0x0001
SWP_NOREDRAW = 0x0008
SWP_FRAMECHANGED = 0x0020

SW_MAXIMIZE = 3
SW_NORMAL = 1

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
