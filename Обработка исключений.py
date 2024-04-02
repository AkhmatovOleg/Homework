def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f"Ошибка: невозможно преобразовать '{s}'в целое число."


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: файл '{filename}' не найден."
    except IOError:
        return f"Ошибка ввода/вывода при работе с файлом '{filename}'."


def divide_number(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."
    except TypeError:
        return "Ошибка: аргументы должны быть числами"


def access_list_element(lst, index):
    try:
        return lst(index)
    except IndexError:
        return f"Ошибка: индекс {index} вне диапазона списка"
    except TypeError:
        return "Ошибка: индекс должен быть целым числом"


s = "wer"
print(string_to_int(s))
filename = 'filename.txt'
print(read_file(filename))
a = 10
b = 0
print(divide_number(a, b))
lst = (1, 3, 4)
index = 5
print(access_list_element(lst, index))
