import warnings


def division(a, b):
    while b > 0:
        b -= 0.01
        print(a / b)
        print(f'b равно:{b}')
        warnings.warn('На ноль делить нельзя', category=UserWarning)


a = 1
b = 1
# print("Фильтр 'error'")
# warnings.simplefilter("error", UserWarning)
# division(a, b)

# print("Фильтр 'ignore'")
# warnings.simplefilter("ignore", UserWarning)
# division(a, b)

print("Фильтр 'always'")
warnings.simplefilter("always",UserWarning)
division(a, b)
