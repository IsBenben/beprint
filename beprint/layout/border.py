# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from .panel import *
from .base import *
from .chars import *
from ..ansi import *

def border(style: Chars, width: int = width, height: int = height, title: str = '') -> str:
    title = title.center(width - 2, style.top)
    lines = []

    for i in range(1, height + 1):
        last_line = []
        lla = last_line.append
        for j in range(1, width + 1):
            if i == 1:
                if j == 1:
                    lla(style.top_left)
                elif j == width:
                    lla(style.top_right)
                else:
                    lla(title[j - 1 - 1])
            elif i == height:
                if j == 1:
                    lla(style.bottom_left)
                elif j == width:
                    lla(style.bottom_right)
                else:
                    lla(style.bottom)
            else:
                if j == 1:
                    lla(style.left)
                elif j == width:
                    lla(style.right)
                else:
                    lla(' ')
        lines.append(''.join(last_line))
    return '\n'.join(lines)

def border_panel(style: Chars, left: int = 1, top: int = 1, width: int = width, height: int = height, title: str = '', pad: int = 1) -> Panel:
    Panel(left, top, width, height).print(border(style, left, top, width, height, title))
    return Panel(left + 1 + pad, top + 1 + pad, width - 2 - 2 * pad, height - 2 - 2 * pad)
