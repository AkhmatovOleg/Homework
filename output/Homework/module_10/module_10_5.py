# Выполнение:
# Создайте функцию read_info(name), где name - название файла. Функция должна:
# 1.Создавать локальный список all_data.
# 2.Открывать файл name для чтения.
# 3.Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# 4.Во время считывания добавлять каждую строку в список all_data.
# Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
# 1.Создайте список названий файлов в соответствии с названиями файлов архива.
# 2.Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его
# в консоль.
# 3.Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with
# и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов.
# Измерьте время выполнения и выведите его в консоль.
import multiprocessing
import time
from datetime import datetime


def read_info(filename):
    all_data = []
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    time_start = datetime.now()
    for filename in filenames:
        read_info(filename)
    time_end = datetime.now()
    print(time_end - time_start)

    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start)
