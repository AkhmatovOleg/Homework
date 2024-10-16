def custom_write(file_name, strings):
    string_positions = {}
    string_number = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        byte_position = file.tell()
        string_number += 1
        file.write(string + '\n')
        string_positions[(string_number, byte_position)] = string
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)