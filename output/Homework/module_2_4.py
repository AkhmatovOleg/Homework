numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    k = 0
    for j in range(1, i + 1):
        if i % j == 0:
            k += 1
    if k == 2:
        is_prime = True
        primes.append(i)
    elif i != 1:
        is_prime = False
        not_primes.append(i)


print(primes)
print(not_primes)
