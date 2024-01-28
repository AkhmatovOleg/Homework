def print_param(a=1, b='строка', c=True):
    print('первый параметр:', a)
    print('второй параметр:', b)
    print('третий параметр:', c)
    return a, b, c


print_param()
print_param(2)
print_param(7, 'точка')
print_param(b=25)
print_param(c=[1, 2, 3])


values_list = [3, 'запятая', False]
values_dict = {'a': 4, 'b': 'многоточие', 'c': True}
res = print_param(*values_list)
print(res)
res1 = print_param(**values_dict)
print(res1)


values_list_2 = [5, 'строка2']
res2 = print_param(*values_list_2, 42)
print(res2)
