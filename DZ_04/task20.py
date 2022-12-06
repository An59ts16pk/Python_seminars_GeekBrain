# Задача 5.	Даны два файла, в каждом из которых находится запись
# многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# ======================================================================
# Функция преобразует строку многочлена в словарь, где
# ключ - степень, значение - коэффициент и возвращает словарь.
def FactorPolynomial(p_str):
    factor = {}
    for i in range(len(p_str)):
        temp = p_str[i].split('x')
        if len(temp) == 2 and temp[1] != '':
            factor[int(temp[1][1:])] = int(temp[0])
        elif len(temp) == 2 and temp[1] == '':
            factor[1] = int(temp[0])
        elif len(temp) == 1:
            factor[0] = int(temp[0])
    return factor

# Функция складывает коэффициенты двух многочленов
# по ключам их словарей и возвращает словарь.
def SumFactorPolynomial(fp1, fp2):
    if len(fp1) > len(fp2):
        fp_sum = fp1
        fp = fp2
    else:
        fp_sum = fp2
        fp = fp1
    for key in fp_sum.keys():
        if key in fp.keys():
            fp_sum[key] = fp_sum[key] + fp[key]
    return fp_sum

# Функция из словаря коэффициентов многочлена
# собирает строку многочлена и её возвращает.
def PolynomialStr(ps_dict):
    res_str = ''
    res = []
    for key, value in ps_dict.items():
        if key > 1:
            res.append(f'{value}x^{key}')
        elif key == 1:
            res.append(f'{value}x')
        elif key == 0:
            res.append(f'{value} = 0')
    res_str = ' + '.join(res)
    return res_str


str_list = []
with open('DZ_04/f1.txt') as file1, open('DZ_04/f2.txt') as file2:
    str_list.append(file1.read()[:-4])
    str_list.append(file2.read()[:-4])

f_p1 = FactorPolynomial(str_list[0].split(' + '))
f_p2 = FactorPolynomial(str_list[1].split(' + '))
print()
print(f_p1)
print(f_p2)

sum_fp = SumFactorPolynomial(f_p1, f_p2)
print()
print(sum_fp)

str_pol = PolynomialStr(sum_fp)
print()
print(str_pol)

with open('DZ_04/sum_polyn.txt', 'w') as file:
    file.write(str_pol)
