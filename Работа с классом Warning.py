import warnings
def division(a, b):
    while b > 0:
        b = b - 0.01
        print(a/b)
    if b == 0:
        warnings.warn('На ноль делить нельзя',category=UserWarning)
    print(f'b равно:{b}')



a = 3
b = 3
print(division(a, b))
