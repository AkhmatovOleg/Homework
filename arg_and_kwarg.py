def test(*arg):
    print('test =', arg)


test(2, 3, 4, 'str', True)


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1


print(factorial(4))
