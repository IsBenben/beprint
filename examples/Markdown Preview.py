from beprint import *

clear_screen()

md = open('README.md', 'r', encoding='utf-8').read()
width = min(terminal_width, 120)
Panel(1, 1, width, terminal_height).print(parse_markdown(md, width), delay=0.01)
