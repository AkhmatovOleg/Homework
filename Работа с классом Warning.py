import warnings


def division(a, b):
    if b == 0:
        warnings.warn('На ноль делить нельзя', category=UserWarning)
        return None
    return a / b


a = 1
b = 1
while b > 0:
    b -= 0.01
    print(a / b)
    print(f'b равно:{b}')
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
