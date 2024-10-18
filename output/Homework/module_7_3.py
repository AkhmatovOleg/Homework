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
                string_punctuation = (',', '.', '=', '!', '?', ';', ':', '-')
                for p in string_punctuation:
                    if p in words_lower:
                        words_lower = words_lower.replace(p, '')
                        words_lower = words_lower.split(' ')
                my_list.append(words_lower)
        all_words[name] = my_list
        return all_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова