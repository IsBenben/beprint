# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from typing import Callable, Sequence, TypeVar
from .base import width, height

T = TypeVar('T')

def columns(left: int = 1, top: int = 1, width: int = width, height: int = height, *, sizes: Sequence[float] | int, callbacks: Sequence[Callable[[int, int, int, int, int], T]]) -> list[T]:
    rounded_width = width + 0.5
    if isinstance(sizes, int):
        sizes = [1] * sizes
    sum_sizes = sum(sizes)
    ratios = [i / sum_sizes for i in sizes]
    remainder_size = 0
    result = []
    current_left = left
    for i, (callback, ratio) in enumerate(zip(callbacks, ratios)):
        remainder_size += ratio * rounded_width
        real_size = int(remainder_size)
        remainder_size -= real_size
        result.append(callback(i, current_left, top, real_size, height))
        current_left += real_size
    return result
