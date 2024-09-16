# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

import os

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines

def write_on(line: int, column: int, text: str):
    print(f"\033[{line};{column}H{text}", end="")

def clear_screen():
    print("\033[2J", end="")
