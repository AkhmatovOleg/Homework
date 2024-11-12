import random

number = random.randint(3, 21)

password = ""

for i in range(1, 21):
    for j in range(i + 1, 21):
        pair_sum = i + j
        if number % pair_sum == 0:
            password += f"{i}{j}"

print(number)
print(password)
