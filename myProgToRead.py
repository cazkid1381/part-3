
from encodings import utf_8


my_file = r'C:\Users\Apple\Downloads\archive\Fake.csv'
with open(my_file, 'r', encoding='utf_8') as f:
    my_lines = f.read()
    print(my_lines)
