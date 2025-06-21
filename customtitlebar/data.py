from ctypes import Structure
from ctypes.wintypes import POINT, RECT

WM_NCCALCSIZE = 0x0083
WM_SYSCOMMAND = 0x0112

SC_MOVE = 0xF010

HTCAPTION = 2

SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
SWP_FRAMECHANGED = 0x0020

SW_MAXIMIZE = 3
SW_NORMAL = 1

GWL_WNDPROC = -4

class NCCALCSIZE_PARAMS(Structure):
    _fields_ = [("rgrc", RECT * 3), ("lppos", POINT)]
