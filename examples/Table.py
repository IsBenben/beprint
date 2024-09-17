from beprint import *

clear_screen()

# Tabel
t = Table(['Name', 'Age', 'Gender'])
t.from_list(
    [['John', '25', 'Male'],
     ['Jane', '30', 'Female'],
     ['Bob', '40', 'Male'],
     ['Alice', '20', 'Female'],
     ['Tom', '35', 'Male']])
t.print(Chars())
