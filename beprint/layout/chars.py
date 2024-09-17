# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from ..ansi import Ansi

style_1 = '┌┬┐├┼┤└┴┘|-'
style_2 = '╓╥╖╟╫╢╙╨╜|-'
style_3 = '╒╤╕╞╪╡╘╧╛|-'
style_4 = '+++++++++|-'

class Chars:
    def __init__(self, chars: str = style_1, style: Ansi = Ansi.reset()):
        self.chars = chars
        self.style = style

    @staticmethod
    def _at(i):
        return property(lambda self: self.chars[i])

    left_top = lt = top_left = tl = _at(0)
    top = t = top_mid = tm = mid_top = mt = _at(1)
    right_top = rt = top_right = rt = _at(2)
    left = l = left_mid = lm = mid_left = ml = _at(3)
    center = c = mid = m = _at(4)
    right = r = right_mid = rm = mid_right = mr = _at(5)
    left_bottom = lb = bottom_left = bl = _at(6)
    bottom = b = bottom_mid = bm = mid_bottom = mb = _at(7)
    right_bottom = rb = bottom_right = br = _at(8)
    vertical = v = _at(9)
    horizontal = h = _at(10)
