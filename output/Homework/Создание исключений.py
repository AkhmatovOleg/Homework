class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


try:
    raise InvalidDataException('Недопустимые данные')
except InvalidDataException as exc:
    print(f'Поймано исключение: {exc}')
    raise ProcessingException('Обработать исключение')

