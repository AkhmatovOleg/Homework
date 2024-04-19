import warnings


def division(a, b):
    while b > 0:
        b -= 0.01
        print(a / b)
        print(f'b равно:{b}')
    if b <= 0.01:
        warnings.warn('На ноль делить нельзя', category=UserWarning)
        return None


a = 1
b = 1
print("Фильтр 'error'")
warnings.simplefilter("error", UserWarning)
division(a, b)
print(division(a, b))

print("Фильтр 'ignore'")
warnings.simplefilter("ignore", UserWarning)
division(a, b)
print(division(a, b))

print("Фильтр 'always'")
warnings.simplefilter("always",UserWarning)
division(a, b)
print(division(a, b))
