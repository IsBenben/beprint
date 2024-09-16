# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from typing import Any
from .layout.panel import *
from .ansi import *

class BeprintStyle:
    string = Ansi.string('cyan')
    number = Ansi.string('blue')
    true = Ansi.string('green').style('italic')
    false = Ansi.string('red').style('italic')
    none = Ansi.string('magenta').style('italic')
    symbol = Ansi.string('black').light().style('bold')
    obj = Ansi.string('yellow')

def beprint(obj: Any, panel: Optional[Panel] = None):
    i = '  '
    def _bp(obj: Any, indent: str = ''):
        repr_obj = repr(obj)
        if isinstance(obj, bool):
            if obj:
                ansi_print(repr_obj, BeprintStyle.true, panel)
            else:
                ansi_print(repr_obj, BeprintStyle.false, panel)
        elif isinstance(obj, str):
            ansi_print(repr_obj, BeprintStyle.string, panel)
        elif isinstance(obj, (int, float)):
            ansi_print(repr_obj, BeprintStyle.number, panel)
        elif obj is None:
            ansi_print(repr_obj, BeprintStyle.none, panel)
        elif isinstance(obj, (list, tuple, set)):
            ansi_print(repr_obj[0] + '\n', BeprintStyle.symbol, panel)
            for item in obj:
                ansi_print(indent + i, BeprintStyle.symbol, panel)
                _bp(item, indent + i)
                ansi_print(',\n', BeprintStyle.symbol, panel)
            ansi_print(indent + repr_obj[-1], BeprintStyle.symbol, panel)
        elif isinstance(obj, dict):
            ansi_print('{\n', BeprintStyle.symbol, panel)
            for key, value in obj.items():
                ansi_print(indent + i, BeprintStyle.symbol, panel)
                _bp(key, indent + i)
                ansi_print(': ', BeprintStyle.symbol, panel)
                _bp(value, indent + i)
                ansi_print(',\n', BeprintStyle.symbol, panel)
            ansi_print(indent + '}', BeprintStyle.symbol, panel)
        else:
            ansi_print(repr_obj, BeprintStyle.obj, panel)
    return _bp(obj)
