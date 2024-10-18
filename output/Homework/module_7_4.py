team1_name = 'Мастера кода'
team1_num = 5
team2_name = 'Волшебники данных'
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 21618.24
task_total = score_1 + score_2
time_avg = (team1_time + team2_time) / task_total
print('В команде %s участников:%s!' % (team1_name, team1_num))
print('Итого сегодня в командах участников:%s и %s!' % (team1_num, team2_num))
print('Команда {} решила задач: {}!'.format(team2_name, score_2))
print('{} решили задачи за {} с'.format(team2_name, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы:{challenge_result}')
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg:10.2f} секунды на задачу')