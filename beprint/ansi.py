# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from __future__ import annotations
from typing import Tuple, Literal, overload, NoReturn, Optional, List
import sys
from .layout.panel import Panel

ansi_color_string_type = \
    Literal['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
style_type = \
    Literal['bold', 'italic', 'underline', 'blink', 'inverse']


class Ansi:
    @overload
    def __init__(self, type: Literal['rgb'], value: Tuple[int, int, int], style: Optional[style_type] = None): ...
    @overload
    def __init__(self, type: Literal['string'], value: Tuple[bool, int], style: Optional[style_type] = None): ...
    @overload
    def __init__(self, type: Literal['reset'], value: None, style: Optional[List[style_type]] = None): ...

    def __init__(self, type, value, style=None):
        self.type = type
        self.value = value
        self.style_value = [] if style is None else style

    @classmethod
    def rgb(cls, r: int, g: int, b: int) -> Ansi:
        return cls('rgb', (r, g, b))

    @classmethod
    def hex(cls, color: str) -> Ansi:
        color = color.removeprefix('#')
        r, g, b = int(color[:2], 16), int(color[2:4], 16), int(color[4:], 16)
        return cls.rgb(r, g, b)

    @overload
    def style(self: Ansi, style: style_type) -> Ansi: ...  # type: ignore
    @overload
    @classmethod
    def style(cls, type: style_type) -> Ansi: ...

    def style(first_arg, second_arg=None) -> Ansi:  # type: ignore
        if isinstance(first_arg, Ansi):
            # Instance method
            return Ansi(first_arg.type, first_arg.value, first_arg.style_value + [second_arg])  # type: ignore
        else:
            # Class method
            return Ansi.reset().style(first_arg)  # type: ignore

    @classmethod
    def string(cls, s: ansi_color_string_type) -> Ansi:
        color_map: dict[ansi_color_string_type, int] = {
            'black': 30,
            'red': 31,
            'green': 32,
            'yellow': 33,
            'blue': 34,
            'magenta': 35,
            'cyan': 36,
            'white': 37,
        }
        return cls('string', (False, color_map[s]))

    @classmethod
    def reset(cls) -> Ansi:
        return cls('reset', None)

    def light(self) -> Ansi | NoReturn:
        if self.type == 'rgb':
            raise ValueError('Cannot light rgb color')
        if self.type == 'string':
            if self.value[0]:
                raise ValueError('Cannot light already light color')
            return Ansi('string', (True, self.value[1] + 60))
        if self.type == 'reset':
            raise ValueError('Cannot light reset color')
        if self.type == 'style':
            raise ValueError('Cannot light style color')
        raise ValueError('Invalid ansi type')

    @property
    def code(self) -> str:
        if self.type == 'rgb':
            r, g, b = self.value
            result = f'\033[38;2;{r};{g};{b}m'
        elif self.type == 'string':
            result = f'\033[{self.value[1]}m'
        elif self.type == 'reset':
            result = '\033[0m'
        else:
            raise ValueError('Invalid ansi type')
        if self.style_value is not None:
            style_map: dict[style_type, int] = {
                'bold': 1,
                'italic': 3,
                'underline': 4,
                'blink': 5,
                'inverse': 7,
            }
            for style in self.style_value:
                result += f'\033[{style_map[style]}m'
        return result

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

def ansi_print(text: str, color_code: Ansi = Ansi.reset(), panel: Optional[Panel] = None):
    if panel:
        _print_func = panel.print
    else:
        _print_func = lambda x: print(x, end='')

    if ansi_support:
        _print_func('{}{}{}'.format(color_code.code, text, Ansi.reset().code))
    else:
        _print_func(text)
