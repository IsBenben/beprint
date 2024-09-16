from beprint import *

clear_screen()

# Printing Objects
beprint({
    'name': 'Alice',
    'age': 20,
    'gender': 'female',
    'hobbies': { 'reading', 'running', 'painting' },
    'is_student': False,
    ('friends', 2): [
        {
            'name': 'Bob',
            'age': 25,
            'best_friend': True
        },
        {
            'name': 'Charlie',
            'age': 30,
            'best_friend': False
        }
    ],
    'address': {
        'country': 'China',
        'city': 'Beijing',
        'street': object(),
        'zip_code': None
    }
}, border(Chars(style_1), 1, 1, width, height, 'Object'))
beprint(locals())
