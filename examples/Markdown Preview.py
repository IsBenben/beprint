from beprint import *

clear_screen()

md = open('README.md', 'r', encoding='utf-8').read()
width = min(width, 120)
Panel(1, 1, width, height).print(parse_markdown(md, width), delay=0.01)
