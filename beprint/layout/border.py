# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from .panel import *
from .base import *
from .chars import *
from ..ansi import *

def border(style: Chars, left: int = 1, top: int = 1, width: int = width, height: int = height, title: str = '', pad: int = 1):
    bottom = top + height - 1
    right = left + width - 1
    title = title.center(width - 2, style.top)

    write_on(top, left, style.top_left)
    write_on(top, right, style.top_right)
    write_on(bottom, left, style.bottom_left)
    write_on(bottom, right, style.bottom_right)
    for idx, i in enumerate(range(left + 1, right)):
        write_on(top, i, title[idx])
        write_on(bottom, i, style.bottom)
    for i in range(top + 1, bottom):
        write_on(i, left, style.left)
        write_on(i, right, style.right)
    
    return Panel(left + 1 + pad, top + 1 + pad, width - 2 - 2 * pad, height - 2 - 2 * pad)
