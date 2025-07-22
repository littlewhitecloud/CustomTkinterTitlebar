# ------------------------
#  CustomTkinterTitlebar
#   By Littlewhitecloud
# ------------------------

__version__ = "1.0.8.7"
__author__ = "littlewhitecloud"

from sys import platform

if platform != "win32":
    raise OSError("Use win32 platform to import this package")

from .titlebar import *

del platform
