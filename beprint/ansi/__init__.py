# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

import sys
from .ansi import *
from ..layout.panel import *
from typing import Optional

ansi_support = True

if sys.platform == 'win32':
    try:
        # https://stackoverflow.com/questions/36760127/...
        # how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console
        from ctypes import windll
        kernel32 = windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except:
        ansi_support = False

def ansi_print(text: str, color_code: Ansi, panel: Optional[Panel] = None):
    if panel:
        _print_func = panel.print
    else:
        _print_func = lambda x: print(x, end='')

    if ansi_support:
        _print_func('{}{}{}'.format(color_code.code, text, Ansi.reset().code))
    else:
        _print_func(text)
