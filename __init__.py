# ------------------------
#  CustomTkinterTitlebar
#   By Littlewhitecloud
# ------------------------

__version__ = "1.0.7.8"
__author__ = "littlewhitecloud"

import sys

if sys.platform != "win32":
	raise OSError("Platform isn't win32(Windows)")
else:
	from .titlebar import *

del sys
