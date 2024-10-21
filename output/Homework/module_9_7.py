# Задание:
# Напишите 2 функции:
# 1.Функция, которая складывает 3 числа (sum_three)
# 2.Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.

def is_prime(func):
    def wrapper(a, b, c):
        numbers = func(a, b, c)
        k = 0
        for j in range(1, numbers + 1):
            if numbers % j == 0:
                k += 1
        if k == 2:
            print('Простое')

        elif numbers != 1:
            print('Составное')
        else:
            print('Ни то, не другое')
        return numbers
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример:
result = sum_three(2, 3, 6)
print(result)
