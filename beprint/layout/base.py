# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

import os

terminal_size = os.get_terminal_size()
terminal_width = terminal_size.columns
terminal_height = terminal_size.lines

def write_on(line: int, column: int, text: str) -> None:
    print(f'\033[{line};{column}H{text}', end='', flush=True)

def clear_screen() -> None:
    print('\033[2J', end='')

def _char_width(c: str) -> int:
    if c == '\t':
        return 4
    if ord(c) < 256:
        return 1
    table_str = '┌┬┐├┼┤└┴┘╓╥╖╟╫╢╙╨╜╒╤╕╞╪╡╘╧╛'
    if c in table_str:
        return 1
    return 2

def text_width(text: str) -> int:
    return sum(_char_width(c) for c in text)

def at_width(text: str, index: int) -> str:
    current = 0
    for i, c in enumerate(text):
        current += _char_width(c)
        if current - 1 == index:
            return c
        elif current - 1 > index:
            return ''
    raise IndexError('Index out of range')
