# задача 1. Фабрика функций
def math_function(y):
    if y == "деление":
        def division(x, y):
            return x / y

        return division
    elif y == "умножение":
        def multiplication(x, y):
            return x * y

        return multiplication
    else:
        raise Exception('Я могу только умножать и делить')


# my_func_division = math_function("деление")
# print(my_func_division(5, 3))
# my_func_multiplication = math_function("умножение")
# print(my_func_multiplication(6, 2))
# my_func_subtraction = math_function("вычитание")
# print(my_func_subtraction(5, 2))


# задача 2. Лямбда-Функции
division_1 = lambda x, y: x / y
print(division_1(2, 10))


def division_1_def(x, y):
    return x / y


print(division_1_def(2, 10))


# задача 3. Вызываемые объекты
class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.b * self.a


rect_1 = Rect(2, 3)
print(rect_1())
