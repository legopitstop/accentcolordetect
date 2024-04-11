import subprocess
import typing

from . import hex2rgb

__all__ = ["accent", "listener"]


def accent() -> tuple[tuple, str]:
    """
    The accent color as RGB

    :return: Returns the accent color in both hex and rgb form (RGB, HEX)
    :rtype: tuple
    """
    cmd = "defaults read -g AppleAccentColor"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return None
    else:
        hex = None
        out = output.decode("utf-8").strip()
        if out == "nil":
            hex = "#5AC8FA"  # Blue (default)
        else:
            num = int(out)
            if num == -1:
                hex = "#251607"  # graphite
            elif num == 0:
                hex = "#FF3B30"  # red
            elif num == 1:
                hex = "#FF9500"  # orange
            elif num == 2:
                hex = "#FFCC00"  # yellow
            elif num == 3:
                hex = "#4CD964"  # green
            elif num == 5:
                hex = "#5856D6"  # purple
            elif num == 6:
                hex = "#FF2D55"  # pink
        if hex is not None:
            return (hex2rgb(hex), hex)
        return None


def listener(callback: typing.Callable[[str], None]) -> None:
    raise NotImplementedError()
