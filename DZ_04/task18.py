# Задача 3.	Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Пример - [1, 2, 2, 3, 4]  -> [1, 3, 4]
# =============================================================================

nums = [int(i) for i in input("\nВведите последовательность чисел через пробел: ").split()]
print(nums)

nums_dict = {}
for el in nums:
    nums_dict[el] = nums_dict.get(el, 0) + 1

nums_list = []
for key, value in nums_dict.items():
    if value == 1:
        nums_list.append(key)

print(nums_list)
