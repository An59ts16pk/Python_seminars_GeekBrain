# Задача 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
# ============================================================================================
# ОТВЕТ: Первому  игроку  надо первым ходом забрать остаток от целочисленного деления
# имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1
# В дальнейшем первому игроку нужно повторять стратегию.
# Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
# если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19 и так далее..
# ====================================================================================================

import random

print("\nИгра с конфетами - человек против человека.")
print("За один ход можно забрать не более чем 28 конфет.")
print("Все конфеты оппонента достаются сделавшему последний ход.")
name1 = input("\nВведите имя первый игрок: ")
name2 = input("Введите имя второй игрок: ")
#total = int(input("Введите количество конфет: "))
total = 200

first_igrok = random.randint(1, 2)
max_take = 28
step_igrok = 0
if first_igrok == 1:
    print("\n  Первый ход делает игрок: ", name1)
    igrok1, igrok2 = name1, name2
else:
    print("\n  Первый ход делает игрок: ", name2)
    igrok1, igrok2 = name2, name1

print(f"\n        Всего конфет на начало игры: {total}.")
while total > 0:
    if step_igrok == 0:
        print(f"\n{igrok1} можешь взять не более 28 конфет.")
        gamer1 = int(input("Сколько конфет берёш???: "))
        if gamer1 > max_take or gamer1 > total:
            while (gamer1 > max_take or gamer1 > total):
                gamer1 = int(input(f"\n{igrok1} можно взять не более {max_take} или осталось меньше, попробуй ещё раз: "))
        total -= gamer1
        if total > 0:
            print(f"  Осталось конфет: {total}.")
            step_igrok = 1
        else:
            print("  Конфеты закончились.")
    
    if step_igrok == 1:
        print(f"\n{igrok2} можешь взять не более 28 конфет.")
        gamer2 = int(input("Сколько конфет берёш???: "))
        if gamer2 > max_take or gamer2 > total:
            while (gamer2 > max_take or gamer2 > total):
                gamer2 = int(input(f"\n{igrok2} можно взять не более {max_take} или осталось меньше, попробуй ещё раз: "))
        total -= gamer2
        if total > 0:
            print(f"  Осталось конфет: {total}.")
            step_igrok = 0
        else:
            print("  Конфеты закончились.")

if step_igrok == 0:
    print(f"ПОБЕДИЛ {igrok1} - все конфеты твои!!!")
elif step_igrok == 1:
    print(f"ПОБЕДИЛ {igrok2} - все конфеты твои!!!")

# ================================================================
#               Игра человека с ботом.
# ================================================================
print("\nИгра с конфетами - человек против бота.")
print("За один ход можно забрать не более чем 28 конфет.")
print("Все конфеты оппонента достаются сделавшему последний ход.")

name = input("\nВведите имя первого игрока: ")
bot = "Компьютер" 
print(f"Имя второго игрока - {bot}")
players = [name, bot]
igrok = random.randint(-1, 0)
totalb = 200
maxtake = 28
print(f"\nСлучайным образом определяем кто ходит первым и это - {players[igrok+1]}")

# Простой бот.
# while totalb > 0:
#     
#     igrok += 1
#     if players[igrok % 2] == bot:
#         print(f"\n    Ходит {players[igrok%2]} и на кону {totalb} конфет.")
#         if totalb <= 28:
#             step = totalb
#         else:
#             step = random.randint(1, 28)
#         print(f"    Компьютер взял {step} конфет.")
#     else:
#         step = int(input(f"\nВаш ход {players[igrok%2]}, на кону {totalb} конфет. Сколько берёш?: "))
#         while step > maxtake or step > totalb:
#             print(f"За один ход можно взять {maxtake} конфет или их на кону осталось меньше.")
#             step = int(input(f"Попробуй ещё раз: "))
#         print(f"{name} взял {step} конфет.")
#     totalb -= step
# print(f"\nОсталось конфет {totalb}. ПОБЕДИЛ {players[igrok%2]}")

# Бот с интелектом.
temp = 0
count = 0
while totalb > 0:
    
    igrok += 1
    if players[igrok % 2] == bot:
        print(f"\n    Ходит {players[igrok%2]} и на кону {totalb} конфет.")
        if totalb <= 28:
            step = totalb
        if count == 0:
            step = totalb % (maxtake + 1)
        else:
            step = maxtake + 1 - temp
        print(f"    Компьютер взял {step} конфет. (Ход {count})")
        count += 1
    else:
        step = int(input(f"\nВаш ход {players[igrok%2]}, на кону {totalb} конфет. Сколько берёш?: "))
        while step > maxtake or step > totalb:
            print(f"За один ход можно взять {maxtake} конфет или их на кону осталось меньше.")
            step = int(input(f"Попробуй ещё раз: "))
        temp = step
        print((f"{name} взял {step} конфет.(Ход {count})"))
        count += 1
    
    totalb -= step

print(f"\nОсталось конфет {totalb}. ПОБЕДИЛ {players[igrok%2]}!!!")
