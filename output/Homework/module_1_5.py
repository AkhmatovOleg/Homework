immutable_var = (1, 'oleg', True)
print(immutable_var)
#immutable_var.append(False)
# потому что кортеж неизменяемый объект
mutable_list = [1, 2, 'oleg', False]
print(mutable_list)
mutable_list[1] = 'lena'
print(mutable_list)
mutable_list.append(12)
print(mutable_list)

