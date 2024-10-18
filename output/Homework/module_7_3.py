class WordsFinder:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        name = self.file_name
        my_list = []
        with open(name, encoding='utf-8') as file:
            for line in file:
                words_lower = line.lower()
                string_punctuation = (',', '.', '=', '!', '?', ';', ':', '-', '', '—', '\n' )
                for p in string_punctuation:
                    if p in words_lower:
                        words_lower = words_lower.replace(p, '')
                words_lower = words_lower.split(' ')
                my_list.extend(words_lower)
        all_words[name] = my_list
        return all_words

    def find(self, word):
        word = word.lower()
        words = self.get_all_words()
        name = self.file_name
        words_list = words[name]
        if word in words_list:
            position = words_list.index(word)
            return {name: position + 1}
        else:
            return f'{word} -  такого слова в списке нет'

    def count(self, word):
        word = word.lower()
        words = self.get_all_words()
        name = self.file_name
        words_list = words[name]
        word_count = 0
        for i in words_list:
            if i == word:
                word_count += 1
        return {name: word_count}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
#
# finder1 = WordsFinder('Rudyard Kipling - If.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
#
# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
