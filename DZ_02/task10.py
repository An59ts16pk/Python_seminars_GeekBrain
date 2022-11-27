# Задача 5.	Реализуйте алгоритм перемешивания списка 
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).
# ==========================================================================

import random

print("\nВариант 1.")

num_list = []
num = int(input("\nВведите число элементов списка: "))
for i in range(10, num+10):
    num_list.append(i)

print(num_list)

for i in range(len(num_list)-1, 0, -1):
    j = random.randint(0, i)
    num_list[i], num_list[j] = num_list[j], num_list[i]

print(num_list)

# ===========================================================
print("\nВариант 2.\n")

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(test_list)
res = random.sample(test_list, len(test_list))
print(res)

# ===========================================================
print("\nВариант 3.")

n_list = []
num = int(input("\nВведите число элементов списка: "))
for i in range(10, num+10):
    n_list.append(i)

print(n_list)

i_list = []
for i in range(num // 2):
    if i not in i_list:
        i_list.append(i)
    n = random.randint(0, num-1)
    while n in i_list:
        n = random.randint(0, num-1)
    i_list.append(n)
    n_list[i], n_list[n] = n_list[n], n_list[i]

print(n_list)
