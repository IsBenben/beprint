from beprint import *

clear_screen()

# Tabel
result = columns(3, 3, terminal_width - 4, terminal_height - 4, sizes=2, callbacks=[
    lambda _, *args: border_panel(Chars(style_1), *args, title='English'),
    lambda _, *args: border_panel(Chars(style_1), *args, title='中文'),
])
t1 = Table(   ['Name',  'Age', 'Gender'])
t1.from_list([['John',  '25',  'Male'  ],
             ['Jane',  '30',  'Female'],
             ['Bob',   '40',  'Male'  ],
             ['Alice', '20',  'Female'],
             ['Tom',   '35',  'Male'  ]])
t1.print(Chars(style=Ansi.string('cyan')), result[0])

t2 = Table(   ['姓名',  '年龄', '性别'])
t2.from_list([['John',  '25',   '男'  ],
              ['Jane',  '30',   '女'  ],
              ['Bob',   '40',   '男'  ],
              ['Alice', '20',   '女'  ],
              ['Tom',   '35',   '男'  ]])
t2.print(Chars(style=Ansi.string('cyan')), result[1])
