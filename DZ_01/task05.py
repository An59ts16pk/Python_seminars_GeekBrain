# Задача 5. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# ===================================================================

print("\nВведите координаты двух точек строкой - например: A (x,y); B (x,y)")
dot = input("\nВведите координаты: ").split('; ')

points = []
for i in range(len(dot)):
    string = ''
    for char in dot[i]:
        if char.isdigit() or char == ',' or char == '-' :
            string += char
    st_list = string.split(',')
    for num in st_list:
        points.append(int(num))
#print(points)

distance = round(((points[2] - points[0])**2 + (points[3] - points[1])**2)**0.5, 2)
print("  Расстояние между двумя точками на координатной плоскости: ", distance)
