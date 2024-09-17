# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from .panel import Panel
from .base import terminal_width, terminal_height, at_width
from .chars import Chars
from .align import align_center
from ..ansi import Ansi

def border(chars: Chars, width: int = terminal_width, height: int = terminal_height, title: str = '') -> str:
    title = align_center(title, width - 2, fill=chars.horizontal)
    lines = []

    for i in range(1, height + 1):
        last_line = []
        lla = last_line.append
        for j in range(1, width + 1):
            if i == 1:
                if j == 1:
                    lla(chars.style.code + chars.top_left)
                elif j == width:
                    lla(chars.top_right + Ansi.reset().code)
                else:
                    lla(at_width(title, j - 2))
            elif i == height:
                if j == 1:
                    lla(chars.style.code + chars.bottom_left)
                elif j == width:
                    lla(chars.bottom_right + Ansi.reset().code)
                else:
                    lla(chars.horizontal)
            else:
                if j == 1:
                    lla(chars.style.code + chars.vertical + Ansi.reset().code)
                elif j == width:
                    lla(chars.style.code + chars.vertical + Ansi.reset().code)
                else:
                    lla(' ')
        lines.append(''.join(last_line))
    return '\n'.join(lines)

def border_panel(chars: Chars, left: int = 1, top: int = 1, width: int = terminal_width, height: int = terminal_height, title: str = '', pad: int = 1, outer_config=None) -> Panel:
    if outer_config is None:
        outer_config = {}
    Panel(left, top, width, height).print(border(chars, width, height, title), **outer_config)
    return Panel(left + 1 + pad, top + 1 + pad, width - 2 - 2 * pad, height - 2 - 2 * pad)
