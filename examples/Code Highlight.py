from beprint import *

clear_screen()

# Code Highlight
code = """
def hello_world(*args):
    print('Hello, world!', *args)

# Call the function
hello_world()
"""
print(highlight_code(code, 'python'))
