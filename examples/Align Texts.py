from beprint import *

clear_screen()

lorem = 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. In quisquam commodi odio atque ab architecto repellat, aperiam eum, vel modi ad non at veniam error, rerum unde explicabo enim optio!'

def create_panel(text, func):
    return lambda _, left, top, width, height: border_panel(Chars(), left, top, width, height, text).print(func(lorem, width - 4))

columns(1, 1, terminal_width, terminal_height, sizes=4, callbacks=[
    create_panel('Left 居左', align_left),
    create_panel('Right 居右', align_right),
    create_panel('Center 居中', align_center),
    create_panel('Stretch 拉伸', align_stretch)
])
