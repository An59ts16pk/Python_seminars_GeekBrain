# Задача 3.	Создайте программу для игры в "Крестики-нолики".
# ===========================================================

import random

# Функция выводит в консоль игровое поле.
def board_prn():
    brd = list(range(1, 10))
    print("+{}+{}+{}+".format('-' * 9, '-' * 9, '-' * 9))
    for i in range(3):
        print("|{: ^9}|{: ^9}|{: ^9}|".format(board_list[brd[0+i*3]], board_list[brd[1+i*3]],
            board_list[brd[2+i*3]]))
        print("+{}+{}+{}+".format('-' * 9, '-' * 9, '-' * 9))

# Функция определяет - клетка занята или свободна.
def check_cell(num_cell):
    sign_pl = ['0', 'X'] # клетка занята знаком
    
    zn1 = sign_pl[0]
    zn2 = sign_pl[1]
    if board_list[num_cell] == zn1 or board_list[num_cell] == zn2:
        print('Клетка номер: ', num_cell, '- занята. Введите другой номер от 1 до 9!')
        return False
    return True

# Функция определяет победные комбинации клеток.
def check_win():
        win_comb = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (3, 5, 7), (1, 5, 9))
        for i_cell in win_comb:
            if board_list[i_cell[0]] == board_list[i_cell[1]] == board_list[i_cell[2]]:
                return board_list[i_cell[0]]
        return False

board_list = {1: '1 cell', 2: '2 cell', 3: '3 cell', 4: '4 cell', 5: '5 cell', 6: '6 cell', 7: '7 cell',
                  8: '8 cell', 9: '9 cell'}
    

print('\nИгра "Крестики - Нолики" на два игрока.\n')

name_1 = input('Первый игрок - Введите Ваше имя: ')
name_2 = input('Второй игрок - Введите Ваше имя: ')
player_1 = ['0']
player_2 = ['X']
player_1.append(name_1)
player_2.append(name_2)
print(' ', player_1[1], 'ваш знак в игре: ', player_1[0], '\n ', player_2[1], 'ваш знак в игре: ', player_2[0])
num = random.randint(1, 2)
if num == 1:
    gamer_1 = player_1
    gamer_2 = player_2
else:
    gamer_1 = player_2
    gamer_2 = player_1
print('Выбираем случайно - за кем будет первый ход: Это {} игрок - {} начинает игру.'.format(num, gamer_1[1]))
br = board_prn()
print('Игрок вводит число от 1 до 9 - номер клетки, куда ставится Ваш знак.\n')

flag = True
count = 0
while flag:
    for i_gamer in range(1, 3):
        if count == 9:
            print('Ничья. Общее кол-во ходов - 9.')
            flag = False
            break
        count += 1
        if i_gamer == 1:
            gamer = gamer_1
        else:
            gamer = gamer_2
        print('{} Ваш ход (ваш знак {}):'.format(gamer[1], gamer[0]))

        while True:
            player_answer = input('    Введите число от 1 до 9: ')
            if '1' <= player_answer <= '9':
                pl_answer = int(player_answer)
                if check_cell(pl_answer):
                    board_list[pl_answer] = gamer[0]
                    print('    {} Вы успешно сделали ход в клетку номер: {}'.format(gamer[1], pl_answer))
                    break
                else:
                    print('    {} Сделайте ход в другую клетку.'.format(gamer[1]))
            else:
                print('Вы ввели неизвестный знак. Введите число от 1 до 9 - номер клетки.')

        symbol = check_win()
        board_prn()
        if symbol == gamer[0]:
            print('      Ура. Победил {} за {} ходов'.format(gamer[1], count))
            print('      Конец игры.')
            flag = False
            break
