# import requests
#
# url = 'https://api.github.com'
#
# try:
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print(f'Ошибка: {response.status_code}')
# except requests.exceptions.RequestException as e:
#     print(f'Что-то пошло не так: {e}')
#
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
added = numbers + 10
subtracted = numbers - 5
multiplied = numbers * 2
divided = numbers / 2


print(f"Сложение: {added}")
print(f"Вычитание: {subtracted}")
print(f"Умножение: {multiplied}")
print(f"Деление: {divided}")