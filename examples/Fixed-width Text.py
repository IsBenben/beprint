from beprint import *

clear_screen()

# Fixed-width Text
p = border_panel(Chars(style_1), 2, 2, 20, 15, 'Test')
p.clear()
p.print(Ansi.rgb(0, 128, 128).code + "Hello, world!")
p.print("Hello, world!\n\n")
p.print(Ansi.string('red').light().style('bold').code + "Hello, world!")
p.print("Hello, world!")
p.print(Ansi.reset().code + "Hello, world!")
p.print("Hello, world!")
p.print("Hello, world!")
p.print("Hello, world!")
