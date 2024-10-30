# Дополните метод/функцию так, чтобы он преобразовывал слова, разделенные тире/подчеркиванием,
# в camel case.
# Первое слово в выходных данных должно быть написано заглавными буквами, только если исходное
# слово было написано заглавными буквами (известно как верхний camel case, также часто называемый Pascal case).
# Следующие слова должны всегда быть написаны заглавными буквами.
#
# Примеры
# "the-stealth-warrior" преобразуется в "theStealthWarrior"
#
# "The_Stealth_Warrior" преобразуется в "TheStealthWarrior"
#
# "The_Stealth-Warrior" преобразуется в "TheStealthWarrior"



def to_camel_case(s):
    # Если входная строка пустая, возвращаем пустую строку
    if not s:
        return ""

    # Заменяем тире и подчеркивания на пробелы
    s = s.replace('-', ' ').replace('_', ' ')

    # Разделяем строку на слова
    words = s.split()

    # Преобразуем первое слово, учитывая регистр, и остальное с заглавной буквы
    if words[0][0].islower():
        camel_case_string = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    else:
        camel_case_string = ''.join(word.capitalize() for word in words)

    return camel_case_string

# Примеры использования
print(to_camel_case("the-stealth-warrior"))  # theStealthWarrior
print(to_camel_case("The_Stealth_Warrior"))   # TheStealthWarrior
print(to_camel_case("The_Stealth-Warrior"))   # TheStealthWarrior
print(to_camel_case("the_stealth_warrior"))   # theStealthWarrior
print(to_camel_case(""))                        # возвращает ""