from beprint import *

clear_screen()

# ANSI Codes
msg = 'Hello, world! 你好，世界！\n'

ansi_print(msg, Ansi.string('red').light().style('bold'))
ansi_print(msg, Ansi.style('bold').style('underline'))
ansi_print(msg, Ansi.rgb(0, 128, 128))
