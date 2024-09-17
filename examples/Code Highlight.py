from beprint import *

clear_screen()

# Code Highlight
code = """
def hello_world(*args):
    print('Hello, world! 你好，世界！', *args)

# Call the function 调用函数
hello_world()
"""
print(highlight_code(code, 'python'))
