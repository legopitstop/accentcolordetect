# accentcolordetect

[![PyPI](https://img.shields.io/pypi/v/accentcolordetect)](https://pypi.org/project/accentcolordetect/)
[![Python](https://img.shields.io/pypi/pyversions/accentcolordetect)](https://www.python.org/downloads//)
![Downloads](https://img.shields.io/pypi/dm/accentcolordetect)
![Status](https://img.shields.io/pypi/status/accentcolordetect)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Issues](https://img.shields.io/github/issues/legopitstop/accentcolordetect)](https://github.com/legopitstop/accentcolordetect/issues)

This package allows you to detect the user's accent color on:
- macOS (untested)
- Windows 10+

The main application of this package is to detect the accent color from your GUI Python application and apply the needed adjustments to your interface. Inspired by the [darkdetect](https://pypi.org/project/darkdetect/) package by [Alberto Sottile](https://pypi.org/user/albertosottile/)

## Installation
Install the module with pip:
```bat
pip3 install accentcolordetect
```
Update existing installation: `pip3 install accentcolordetect --upgrade`


## Usage
```Python
import accentcolordetect

>>> accentcolordetect.accent()
((255, 140, 0), '#ff8c00')
```