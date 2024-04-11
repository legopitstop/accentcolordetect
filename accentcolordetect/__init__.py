"""Detects the systems primary accent color"""

import sys

__version__ = "0.0.2"
__all__ = ["rgb2hex", "hex2rgb", "accent", "listener"]


def rgb2hex(rgb: tuple) -> str:
    """
    Converts RGB to HEX value

    :param rgb: The RGB color in tuple form
    :type rgb: tuple
    :return: The RGB color as a HEX
    :rtype: str
    """
    if isinstance(rgb, list):
        rgb = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
    return "#%02x%02x%02x" % rgb


def hex2rgb(hex: str) -> tuple:
    """
    Converts hex value to RGB

    :param hex: The HEX color as a string
    :type hex: str
    :return: The RGB color as a tuple
    :rtype: tuple
    """
    return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))


if sys.platform == "darwin":  # has not been tested on a mac
    from ._darwin_detect import *
elif sys.platform == "win32":
    from ._windows_detect import *
elif sys.platform == "linux":
    from ._dummy import *
else:
    from ._dummy import *
