import random

number = random.randint(3, 20)

password = ""

for i in range(1, 21):
    for j in range(i + 1, 21):
        pair_sum = i + j
        if number % pair_sum == 0:
            password += f"{i}{j}"

print(f'Случайное число: {number}')
print(f'Пароль: {password}')
