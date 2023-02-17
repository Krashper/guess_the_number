import random
def guess_the_number(begin, end):
    players = []
    count_of_players = int(input('Выберите количество игроков:'))
    while count_of_players < 1:
        count_of_players = int(input('Выберите количество игроков:'))
    
    for n in range(1, count_of_players + 1):
        player = input(f'Имя игрока {n}: ')
        players.append(player)
    
    number = random.randint(begin, end)
    cur_pl_index = 0
    current_player = players[cur_pl_index]
    answer = int(input(f'{current_player}, какое число загадал компьютер: '))
    count_of_attempts = 1

    while answer != number:
        if answer < number:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')
        print('Переход хода!')
        cur_pl_index += 1
        if cur_pl_index == len(players):
            cur_pl_index = 0
        current_player = players[cur_pl_index]
        answer = int(input(f'{current_player}, выберите новое число: '))
        count_of_attempts += 1

    print(f'{current_player} отгадал(-a) число {number}')
    print(f'Общее количество попыток: {count_of_attempts}')