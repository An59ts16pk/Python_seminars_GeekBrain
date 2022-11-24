# Задача 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ - not, ⋁ - or, ⋀ - and
# количество возможных значений - 8 (2**3 = 8)
# ===================================================================

count = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not(x or y or z) == (not x and not y and not z)
            if result == True:
                count += 1
                print(result)
            else:
                print(result)
if count == 8:
    print("\n  Предикат истинный для всех значений.")
else:
    print("\n  Предикат неверен.")
