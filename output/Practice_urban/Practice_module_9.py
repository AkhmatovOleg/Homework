# 1. Написать функцию которая возвращает функцию повторения двух первых символов n  раз.
# 2. Создать массив функций и применить все функции поочередно к аргументу.
# 3. Применить все функции поочередно к массиву аргументов.
animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']


# 1

def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal

    return repeat


test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))

# 2

repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)

# 3

fin_result = [func(x) for func in repetitions for x in animals]
print(fin_result)


# Задача - есть функция, которая возвращает результат введения числа а в степень b.
# Нужно ускорить ее, чтобы она не делала повторные вычисления

def memoize_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргументами= {args}, внутренняя память= {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилпсь, ответ = {mem[args]}'
        else:
            return f'Функция уже была вополнена ренее, ответ = {mem[args]}'

    return wrapper


@memoize_func
def func(a, b):
    print(f'Выполняем функцию с аргументами {a}, {b}')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
