# import zipfile
#
#
# zip_file_name = 'voina_i_mir.zip'
#
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     zfile.extract(filename)
#
#
from pprint import pprint
from random import randint

filename = '90202836.txt'

stat = {}
# stat = {'а': {'т': 500, 'х': 5, }, 'т': {'о': 100, 'у': 50, }}

sequence = ''
with open(filename, 'r', encoding='cp1251') as file:
    for line in file:
        # print(line)
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char

pprint(stat)
pprint(len(stat))

totals = {}
stat_for_generate = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

N = 1000
printed = 0

sequence = ''
while printed < N:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    sequence = sequence[1:] + char