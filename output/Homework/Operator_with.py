file_name = 'poem_2.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line, end='')
print(file.closed)

