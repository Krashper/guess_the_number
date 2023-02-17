import random
def guess_the_number(begin, end):
    number = random.randint(begin, end)
    answer = int(input('Какое число загадал компьютер:'))
    while answer != number:
        if answer < number:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')
        print('Переход хода!')
        answer = int(input('Выберите новое число:'))
    print(f'Вы отгадали число {number}')