def exp(x):
    return x**2
def odd_number(x):
    return x%2

mu_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(exp,filter(odd_number, mu_numbers))
print(list(result))