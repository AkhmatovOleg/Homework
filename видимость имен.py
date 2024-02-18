def test_function():
    inner_function()


def inner_function():
    def test_function_2():
        print('Я в области видимости функции test_function')


inner_function()