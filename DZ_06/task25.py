# Задача 1. В модуле math есть функция math.gcd(a, b), возвращающая
# наибольший общий делитель (НОД) двух чисел. Вычислите и напечатайте
# наибольший общий делитель для списка натуральных чисел. Ввод чисел 
# продолжается до ввода пустой строки. 
# Входные данные: 36 12 144 18; Выходные данные: 6 
# ====================================================================
from math import gcd
from functools import reduce

#nums = [int(i) for i in input("Введите набор натуральных чисел через пробел: ").split()]
#nums = [36, 12, 144, 18]
nums = [144, 12, 36, 18, 216]

# a = 36
# b = 12
# c = 144
# d = 18
# print()
# print(gcd(a, b)) # 12
# print(gcd(a, c)) # 36
# print(gcd(a, d)) # 18
# print()
# print(gcd(12, 36)) # 12
# print(gcd(12, 18)) # 6
# print()
# print(gcd(12, 6)) # 6
# print()

print("\nВариант 1.")
max_n = max(nums)
nod = []
for i in range(1, max_n+1):
    count = 0
    for j in nums:
        if j % i == 0:
            count += 1
    if count == len(nums):
        nod.append(i)

print(f"Наибольший общий делитель списка натуральных чисел {nums}: {max(nod)}")

# print("\nВариант 2.")
# print(f"Наибольший общий делитель списка натуральных чисел {nums}: ", end='')
# for j in range(len(nums)-1):
#     for i in range(1, len(nums)):
#         nums[i] = gcd(nums[0], nums[i])
#     nums.pop(0)
# print(nums[0])

# print("\nВариант 3.")
# print(f"Наибольший общий делитель списка натуральных чисел {nums}: ", end='')
# for i in range(len(nums)-1):
#     for j in range(1+i, len(nums)):
#         nums[j] = gcd(nums[i], nums[j])
#     #print(nums)
# print(nums[len(nums)-1])

print("\nВариант 4.")
nod4 = reduce(gcd, nums)
print(f"Наибольший общий делитель списка натуральных чисел {nums}: {nod4}")

# print("\nВариант 5.")
# nod5 =  gcd(gcd(gcd(nums[0], nums[1]), nums[2]), nums[3])
# print(f"Наибольший общий делитель списка натуральных чисел {nums}: {nod5}")

print("\nВариант 6.")
nod6 = gcd(nums[0], nums[1])
for i in range(2, len(nums)):
    nod6 = gcd(nod6, nums[i])
print(f"Наибольший общий делитель списка натуральных чисел {nums}: {nod6}")
