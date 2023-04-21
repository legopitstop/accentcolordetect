"""Detects the systems primary accent color"""

__version__ = '0.0.1'

import sys

def rgb2hex(rgb):
    return '%02x%02x%02x' % rgb

def hex2rgb(hex):
    return tuple(int(hex[i:i+2], 16)  for i in (0, 2, 4))

if sys.platform == 'darwin': # has not been tested on a mac
    from ._darwin_detect import *
elif sys.platform == "win32":
    from ._windows_detect import *
elif sys.platform == "linux":
    from ._dummy import *
else:
    from ._dummy import *