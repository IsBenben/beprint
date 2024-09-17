from beprint import *

clear_screen()

# Fixed-width Text
msg = 'Hello, world! 你好，世界！'

p = border_panel(Chars(style_1), 2, 2, 20, 16, 'Test')
p.clear()
p.print(Ansi.rgb(0, 128, 128).code + msg)
p.print(msg + '\n\n')
p.print(Ansi.string('red').light().style('bold').code + msg)
p.print(msg)
p.print(Ansi.reset().code + msg)
p.print(msg)
p.print(msg)
p.print(msg)
