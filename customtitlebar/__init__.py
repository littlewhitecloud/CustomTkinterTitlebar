# ------------------------
#  CustomTkinterTitlebar
#   By Littlewhitecloud
# ------------------------

__version__ = "1.0.8.0"
__author__ = "littlewhitecloud"

from sys import platform

if platform != "win32":
    raise OSError("Platform isn't win32(Windows)")

from .titlebar import CTT
