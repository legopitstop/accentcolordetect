# Accentcolordetect

This package allows you to detect the user's accent color on:
- macOS (untested)
- Windows 10+

The main application of this package is to detect the accent color from your GUI Python application and apply the needed adjustments to your interface. Inspired by the [darkdetect](https://pypi.org/project/darkdetect/) package by [Alberto Sottile](https://pypi.org/user/albertosottile/)

## Usage
```Python
import accentcolordetect

>>> accentcolordetect.accent()
((255, 140, 0), '#ff8c00')
```

## Install
```
pip install accentcolordetect
```