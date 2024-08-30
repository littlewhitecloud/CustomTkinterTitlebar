from ctypes import Structure
from ctypes.wintypes import POINT, RECT

WM_NCCALCSIZE = 0x0083

SWP_NOSIZE = 0x0001
SWP_NOREDRAW = 0x0008
SWP_FRAMECHANGED = 0x0020

SW_MAXIMIZE = 3
SW_NORMAL = 1

GWL_WNDPROC = -4


class NCCALCSIZE_PARAMS(Structure):
    _fields_ = [("rgrc", RECT * 3), ("lppos", POINT)]
