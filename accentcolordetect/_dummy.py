import typing

__all__ = ["accent", "listener"]


def accent() -> None:
    """
    Unsupported platform
    """
    return None


def listener(callback: typing.Callable[[str], None]) -> None:
    raise NotImplementedError()
