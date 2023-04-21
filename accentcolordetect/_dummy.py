import typing

def accent():
    return None

def listener(callback: typing.Callable[[str], None]) -> None:
    raise NotImplementedError()
