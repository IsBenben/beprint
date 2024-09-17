# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

import mistune
from .ansi import *
from .layout.border import *
from .highlight_code import *

def desc(text: str) -> str:
    return Ansi.string('black').light().style('italic').code + text + Ansi.reset().code

class AnsiRenderer(mistune.BaseRenderer):
    """A renderer for converting Markdown to ANSI escape sequences."""
    NAME = 'ansi'

    def __init__(self, width: int):
        super(AnsiRenderer, self).__init__()
        self.width = width

    def render_token(self, token, state):
        # backward compitable with v2
        func = self._get_method(token['type'])
        attrs = token.get('attrs')

        if 'raw' in token:
            text = token['raw']
        elif 'children' in token:
            text = self.render_tokens(token['children'], state)
        else:
            if attrs:
                return func(**attrs)
            else:
                return func()
        if attrs:
            return func(text, **attrs)
        else:
            return func(text)

    def text(self, text: str) -> str:
        return text

    def emphasis(self, text: str) -> str:
        return Ansi.style('italic').code + text + Ansi.reset().code

    def strong(self, text: str) -> str:
        return Ansi.style('bold').code + text + Ansi.reset().code

    def link(self, text: str, url: str, title=None) -> str:
        s = Ansi.string('blue').style('underline').code + url + Ansi.reset().code
        return desc('link[') + s + desc('/') + text + desc(']')

    def image(self, text: str, url: str, title=None) -> str:
        return desc('image[') + url + desc('/') + text + desc(']')

    def codespan(self, text: str) -> str:
        return Ansi.string('cyan').code + text + Ansi.reset().code

    def linebreak(self) -> str:
        return '\n'

    def softbreak(self) -> str:
        return '\n'

    def inline_html(self, html: str) -> str:
        return html

    def paragraph(self, text: str) -> str:
        return '\n  ' + text + '\n'

    def heading(self, text: str, level: int) -> str:
        head_desc = {
            1: desc('TITLE[') + Ansi.style('bold').code + text + Ansi.reset().code + desc(']'),
            2: desc('SUBTITLE[') + Ansi.style('bold').code + text + Ansi.reset().code + desc(']'),
            3: desc('SUBSUBTITLE[') + Ansi.style('bold').code + text + Ansi.reset().code + desc(']'),
            4: desc('SUB*4 TITLE[') + Ansi.style('bold').code + text + Ansi.reset().code + desc(']'),
            5: desc('SUB*5 TITLE[') + Ansi.style('bold').code + text + Ansi.reset().code + desc(']'),
            6: desc('SUB*6 TITLE[') + Ansi.style('bold').code + text + Ansi.reset().code + desc(']'),
        }
        return '\n' + border(Chars(style_4), self.width, 1, head_desc[level]) + '\n'

    def blank_line(self) -> str:
        return ''

    def thematic_break(self) -> str:
        return '\n' + '-' * (self.width // 2) + '\n'

    def block_text(self, text: str) -> str:
        return text

    def block_code(self, code: str, info=None) -> str:
        if info:
            lang = info.split(None, 1)[0]
        else:
            lang = ''
        return '\n' + highlight_code(code, lang) + '\n'

    def block_quote(self, text: str) -> str:
        result = text.split('\n')
        for i, line in enumerate(result):
            result[i] = desc('| ') + line
        return '\n' + '\n'.join(result) + '\n'

    def block_html(self, html: str) -> str:
        return html + '\n'

    def block_error(self, text: str) -> str:
        return Ansi.string('red').code + 'ERR: ' + text + Ansi.reset().code + '\n'

    def list(self, text: str, ordered: bool, **attrs) -> str:
        result = ['']
        number = 1
        for line in text.removesuffix('\n').split('\n'):
            number += 1
            index_str = str(number) + '. ' if ordered else '* '
            result.append(Ansi.style('bold').code + index_str + Ansi.reset().code + line)
        return '\n' + '\n'.join(result) + '\n'

    def list_item(self, text: str) -> str:
        return text + '\n'

def parse_markdown(md, width=width) -> str:
    renderer = AnsiRenderer(width)
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(md)  # type: ignore
