# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from typing import Callable, Literal
from .base import text_width

def _align(text: str, align: Callable[[list[str]], list[str | None]], width: int, fill: str = ' ') -> str:
    def _align_line(line: list[str]) -> str:
        line = [(' ' if i != 0 else '') + word for i, word in enumerate(line)]
        white_line = align(line)
        count = white_line.count(None)
        if count == 0:
            return ' '.join(line)
        real_width = width - sum(text_width(word) for word in white_line if word is not None)
        space_width = (real_width + 0.5) / count
        result = []
        remainder_space = 0
        for word in white_line:
            if word is None:
                remainder_space += space_width
                result.append(fill * int(remainder_space))
                remainder_space -= int(remainder_space)
            else:
                result.append(word)
        return ''.join(result)
    
    lines = text.split('\n')
    result = []
    for line in lines:
        words = line.split(' ')
        line_length = -1
        line_words = []
        for word in words:
            if line_length + text_width(word) >= width:
                # Current line is full
                result.append(_align_line(line_words))
                line_length = -1
                line_words.clear()
            line_words.append(word)
            line_length += text_width(word) + 1
    if line_words:
        result.append(_align_line(line_words))
    return '\n'.join(result)

def align_left(text: str, width: int, fill: str = ' '):
    return _align(text, lambda words: words + [None], width, fill=fill)

def align_center(text: str, width: int, fill: str = ' '):
    return _align(text, lambda words: [None] + words + [None], width, fill=fill)

def align_stretch(text: str, width: int, fill: str = ' '):
    def _convert(words):
        result = []
        for i, word in enumerate(words):
            if i != 0:
                result.append(None)
            result.append(word)
        return result
    return _align(text, _convert, width, fill=fill)

def align_right(text: str, width: int, fill: str = ' '):
    return _align(text, lambda words: [None] + words, width, fill=fill)

align_type = Literal['left', 'center', 'stretch', 'right']

def align(text: str, align: align_type, width: int, fill: str = ' ') -> str:
    if align == 'left':
        return align_left(text, width, fill=fill)
    elif align == 'center':
        return align_center(text, width, fill=fill)
    elif align =='stretch':
        return align_stretch(text, width, fill=fill)
    elif align == 'right':
        return align_right(text, width, fill=fill)
    else:
        raise ValueError(f'Invalid align value: {align}')
