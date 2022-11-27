# Задача 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# ===================================================================================

num = int(input("\nВведите число: "))

num_list = []
for i in range(-num, num+1):
    num_list.append(i)

print(num_list)
print()

mult = 1
i_list = []
file = open('DZ_02/file.txt', 'r')
for i_line in file:
    if 0 <= int(i_line) < len(num_list):
        mult *= num_list[int(i_line)]
    i_list.append(int(i_line))
file.close()

print("Позиции из файла: ", i_list)

print("Произведение элементов списка по позициям из файла =", mult)

