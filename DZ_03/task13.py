# Задача 3.	Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# ====================================================================

num_list = [1.1, 1.2, 3.1, 5, 10.01]

n_list = []
for i in range(len(num_list)):
    temp = round((num_list[i] - int(num_list[i])), 2)
    if temp != 0:
        n_list.append(temp)

print("\nРазница между max и min дробной части чисел: ", max(n_list) - min(n_list))
