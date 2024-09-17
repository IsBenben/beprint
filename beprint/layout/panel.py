# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from .base import terminal_width, terminal_height, write_on, text_width
import time
from typing import Optional

class Panel:
    def __init__(self, left: int = 1, top: int = 1, width: int = terminal_width, height: int = terminal_height):
        self.width = width
        self.height = height
        self.left = self.current_column = left
        self.top = self.current_line = top
        self.is_ansi = False
        self.delay = 0.005
        self.clear_delay = 5

    def print(self, text: str, delay: Optional[float] = None, clear_delay: Optional[float] = None):
        if delay is None:
            delay = self.delay
        if clear_delay is None:
            clear_delay = self.clear_delay
        
        for char in text:
            # Ansi escape sequence support
            if char == '\033':
                print(char, end='')
                self.is_ansi = True
                continue
            if char == 'm' and self.is_ansi:
                print(char, end='')
                self.is_ansi = False
                continue
            if self.is_ansi:
                print(char, end='')
                continue

            if char == '\n':
                self.current_line += 1
                self.current_column = self.left
            elif char == '\r':
                self.current_column = self.left
            elif char == '\b':
                self.current_column -= 1
                if self.current_column < self.left:
                    self.current_column = self.left
                write_on(self.current_line, self.current_column, ' ')
            elif char == '\t':
                self.print('    ')
            else:
                if self.current_column - self.left + text_width(char) > self.width:
                    self.current_line += 1
                    self.current_column = self.left
                if self.current_line - self.top >= self.height:
                    time.sleep(clear_delay)
                    self.clear()
                write_on(self.current_line, self.current_column, char)
                if delay > 0 and char not in ' \n\r\b\t':
                    time.sleep(delay)
                self.current_column += text_width(char)

    def clear(self):
        self.current_line = self.top
        self.current_column = self.left
        self.print(' ' * self.width * self.height, delay=0)
        self.current_line = self.top
        self.current_column = self.left
