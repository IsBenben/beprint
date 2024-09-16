from beprint import *

clear_screen()

# ANSI Codes
ansi_print("Hello, world!\n", Ansi.string('red').light().style('bold'))
ansi_print("Hello, world!\n", Ansi.style('bold').style('underline'))
ansi_print("Hello, world!\n", Ansi.rgb(0, 128, 128))
