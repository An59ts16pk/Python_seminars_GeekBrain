# Задача 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# ================================================================================================
# Функция кодирования строки.
def CodeStr(st):
    cod = ''
    count = 1
    for i in range(1, len(st)):
        if st[i-1] == st[i]:
            count += 1
        else:
            cod += str(count) + st[i-1]
            count = 1
    cod += str(count) + st[-1]
    return cod

# Функция декодирования строки.
def DeCodeStr(st):
    decod = ''
    digit = ''
    for s in st:
        if s.isdigit():
            digit += s
        elif s.isalpha:
            decod += s * int(digit)
            digit = ''
    return decod


origin = ''
with open('DZ_05/original.txt') as f:
    origin = f.read()

print("\nТекст для кодировки: ")
print(origin)

code = CodeStr(origin)

print("\nТекст после кодировки: ")    
print(code)

with open('DZ_05/code.txt', 'w') as f:
    f.write(code)

decode = DeCodeStr(code)

print("\nТекст после дешифровки: ")
print(decode)

with open('DZ_05/decode.txt', 'w') as f:
    f.write(code)
