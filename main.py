from function import guess_the_number

print('Игра началась!')
begin, end = tuple(map(int, input('Выберите диапозон числа (через запятую, например: 1, 10):').split(', ')))
guess_the_number(begin, end)