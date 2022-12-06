# Задача 4.	Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# ===============================================================
import random

degree = [int(i) for i in input("\nВведите натуральную степень для первого и второго многочлена через пробел: ").split()]

factor_list = []
for s in range(len(degree)):
    factor = []
    string = ''
    for i in range(degree[s], -1, -1):
        k = random.randint(0, 100)
        factor.append(k)
        if k != 0:
            if i == degree[s]:
                string += f'{k}x^{i}'
            elif 1 < i < degree[s]:
                string += f' + {k}x^{i}'
            elif i == 1:
                string += f' + {k}x'
            else:
                string += f' + {k} = 0'
        else:
            string += ''
    factor_list.append(factor)

    with open(f'DZ_04/f{s+1}.txt', 'w') as file:
        file.write(string)

print("\nСписок коэффициентов многочленов: ", factor_list)
