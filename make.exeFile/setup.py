# cx_Freeze
# $ python setup.py build

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "CHOOOSEFILE",
version = "1.0",
description = 'converter',
executables = [Executable("main.py", base=base)])
