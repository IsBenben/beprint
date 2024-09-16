from beprint import *

clear_screen()

# 2 Columns Layout
result = columns(3, 3, width - 4, height - 4, sizes=[0.2, 0.8], callbacks=[
    lambda _, *args: border(Chars(style_1), *args, title='Info'),
    lambda _, *args: border(Chars(style_1), *args, title='Contents'),
])
result[0].print('Powered by BePrint')
beprint({
    '//': 'Test comment',
    'string': 'Hello, world!',
    'number': 123,
    'boolean': True,
    'null': None,
    'array': [1, 2, 3],
    'object': object()
}, result[1])
