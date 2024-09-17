from beprint import *

clear_screen()

# Columns Layout
result = columns(3, 3, terminal_width - 4, terminal_height - 4, sizes=[0.2, 0.2, 0.6], callbacks=[
    lambda _, *args: border_panel(Chars(style_1), *args, title='Info 信息'),
    lambda _, *args: border_panel(Chars(style_1), *args, title='Contents 内容'),
    lambda _, *args: border_panel(Chars(style_1), *args, title='Code 代码'),
])
result[0].print('Powered by BePrint!\n由 BePrint 提供支持！')
beprint({
    '//': 'Test comment. 测试注释。',
    'string 字符串': 'Hello, world! 你好，世界！',
    'number 数字': 123,
    'boolean 布尔': True,
    'null 空': None,
    'array 数组': [1, 2, 3],
    'object 对象': object()
}, result[1])
with open(__file__, encoding='utf-8') as f:
    result[2].print(highlight_code(f.read(), 'python'))

write_on(terminal_height, 1, 'Press enter to exit... 按下 Enter 退出……')
input()
