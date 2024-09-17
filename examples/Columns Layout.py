from beprint import *

clear_screen()

# Columns Layout
result = columns(3, 3, width - 4, height - 4, sizes=[0.1, 0.3, 0.6], callbacks=[
    lambda _, *args: border_panel(Chars(style_1), *args, title='Info'),
    lambda _, *args: border_panel(Chars(style_1), *args, title='Contents'),
    lambda _, *args: border_panel(Chars(style_1), *args, title='Code'),
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
with open(__file__, 'r') as f:
    result[2].print(highlight_code(f.read(), 'python'))

write_on(height, 1, 'Press enter to exit...')
input()
