from winreg import HKEY_CURRENT_USER as hkey, QueryValueEx as getSubkeyValue, OpenKey as getKey
import typing

from . import hex2rgb

def accent():
    try:
        key = getKey(hkey, "Software\\Microsoft\\Windows\\DWM")
        subkey = getSubkeyValue(key, "ColorizationColor")[0]
    except FileNotFoundError:
        return None
    hex = str(format(subkey, 'x'))[2:]
    return (hex2rgb(hex), '#'+hex)

def listener(callback: typing.Callable[[str], None]) -> None:
    raise NotImplementedError()