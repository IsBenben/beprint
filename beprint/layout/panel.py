# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from .base import width, height, write_on
import time

class Panel:
    def __init__(self, left: int = 1, top: int = 1, width: int = width, height: int = height):
        self.width = width
        self.height = height
        self.left = self.current_column = left
        self.top = self.current_line = top
        self.is_ansi = False
    
    def print(self, text: str, delay: float = 0.01, clear_delay: float = 3):
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
                if self.current_column - self.left >= self.width:
                    self.current_line += 1
                    self.current_column = self.left
                write_on(self.current_line, self.current_column, char)
                if delay > 0 and char not in ' \n\r\b\t':
                    time.sleep(delay)
                self.current_column += 1
            if self.current_line - self.top >= self.height:
                time.sleep(clear_delay)
                self.clear()

    def clear(self):
        self.current_line = self.top
        self.current_column = self.left
        self.print(' ' * self.width * self.height, delay=0)
        self.current_line = self.top
        self.current_column = self.left
