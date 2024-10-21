# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
#
# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# 1.Напишите функцию-генератор all_variants(text).
# 2.Опишите логику работы внутри функции all_variants.
# 3.Вызовите функцию all_variants и выполните итерации.

def all_variants(text):
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


a = all_variants('abc')
for i in a:
    print(i)
