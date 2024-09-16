# *-* encoding: utf-8 *-*
"""
Copyright (c) 2024, IsBenben and all contributors
Licensed under the Apache License, Version 2.0
"""

from pygments import lex
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.token import Token
from pygments.util import ClassNotFound
from .ansi import *

code_colors = {
    Token.Comment.Multiline: Ansi.hex('#6a9955'),
    Token.Comment.Preproc: Ansi.hex('#c586c0'),
    Token.Comment.PreprocFile: Ansi.hex('#ce9178'),
    Token.Comment.Single: Ansi.hex('#6a9955'),
    Token.Error: Ansi.hex('#f44747').style('underline'),
    Token.Keyword.Constant: Ansi.hex('#569cd6').style('bold'),
    Token.Keyword.Declaration: Ansi.hex('#569cd6').style('bold'),
    Token.Keyword.Namespace: Ansi.hex('#c586c0').style('bold'),
    Token.Keyword.Type: Ansi.hex('#569cd6').style('bold'),
    Token.Keyword: Ansi.hex('#c586c0').style('bold'),
    Token.Literal.Number.Float: Ansi.hex('#b5cea8'),
    Token.Literal.Number.Hex: Ansi.hex('#ce9178'),
    Token.Literal.Number.Integer: Ansi.hex('#b5cea8'),
    Token.Literal.String.Affix: Ansi.hex('#569cd6'),
    Token.Literal.String.Doc: Ansi.hex('#ce9178'),
    Token.Literal.String.Double: Ansi.hex('#ce9178'),
    Token.Literal.String.Escape: Ansi.hex('#d7ba7d'),
    Token.Literal.String.Interpol: Ansi.hex('#569cd6'),
    Token.Literal.String.Single: Ansi.hex('#ce9178'),
    Token.Literal.String: Ansi.hex('#ce9178'),
    Token.Name.Attribute: Ansi.hex('#8cdcfe'),
    Token.Name.Builtin.Pseudo: Ansi.hex('#569cd6').style('italic'),
    Token.Name.Builtin: Ansi.hex('#dcdcaa'),
    Token.Name.Class: Ansi.hex('#4ec9b0'),
    Token.Name.Decorator: Ansi.hex('#dcdcaa'),
    Token.Name.Exception: Ansi.hex('#4ec9b0'),
    Token.Name.Function.Magic: Ansi.hex('#4ec9b0').style('italic'),
    Token.Name.Function: Ansi.hex('#dcdcaa'),
    Token.Name.Label: Ansi.hex('#cccccc'),
    Token.Name.Namespace: Ansi.hex('#4ec9b0'),
    Token.Name.Other: Ansi.hex('#8cdcfe'),
    Token.Name.Tag: Ansi.hex('#8cdcfe'),
    Token.Name.Variable.Magic: Ansi.hex('#8cdcfe').style('italic'),
    Token.Name: Ansi.hex('#8cdcfe'),
    Token.Operator.Word: Ansi.hex('#569cd6').style('bold'),
    Token.Operator: Ansi.hex('#cccccc'),
    Token.Punctuation: Ansi.hex('#cccccc'),
    Token.Text: Ansi.hex('#cccccc'),
}
line_numbers_color = Ansi.hex('#6e7681')
background_color = Ansi.hex('#1f1f1f')

def highlight_code(code, language='', line_numbers=True):
    try:
        lexer = get_lexer_by_name(language)
    except ClassNotFound:
        lexer = guess_lexer(code)
    tokens = list(lex(code, lexer))
    result = ''
    for token in tokens:
        color = code_colors.get(token[0], Ansi.hex('#cccccc'))
        result += color.code + token[1] + Ansi.reset().code
    if line_numbers:
        max_line_length = len(str(len(code.split('\n')))) + 1
        result_lines = result.split('\n')
        format_string = '{}{{:>{}}} {}{{}}'.format(line_numbers_color.code, max_line_length, Ansi.reset().code)
        for i, line in enumerate(result_lines):
            result_lines[i] = format_string.format(i+1, line)
        result = '\n'.join(result_lines)
    return result
