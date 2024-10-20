class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            my_list = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    words_lower = line.lower()
                    string_punctuation = (',', '.', '=', '!', '?', ';', ':', '-', '', '—', '\n')
                    for p in string_punctuation:
                        if p in words_lower:
                            words_lower = words_lower.replace(p, '')
                    words_lower = words_lower.split(' ')
                    my_list.extend(words_lower)
            all_words[file_name] = my_list
        return all_words

    def find(self, word):
        word = word.lower()
        words = self.get_all_words()
        result = {}
        for name, words in words.items():
            if word in words:
                position = words.index(word)
                result[name] = position +1
        return result or f'{word} -  такого слова в списке нет'

    def count(self, word):
        word = word.lower()
        words = self.get_all_words()
        words_count = {}
        for name, words in words.items():
            count = 0
            for i in words:
                if i == word:
                    count += 1
            words_count[name] = count
        return words_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

