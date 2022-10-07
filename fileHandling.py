# ✅ prefix string with r
file_name = r'C:\Users\Apple\Desktop\part 3\myFileToRead.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

