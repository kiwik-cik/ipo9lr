import math
def find_min_angle_point(x1, x2, y1, y2, z1, z2):
#Вычисляем углы между осью абсцисс и каждой точкой
    angle_x = math.atan2(x2, x1)
    angle_y = math.atan2(y2, y1)
    angle_z = math.atan2(z2, z1)
#Поиск минимального угла
    min_angle = min(angle_x, angle_y, angle_z)
#Определение точки с минимальным углом
    if min_angle == angle_x:
        return (x1, x2)
    elif min_angle == angle_y:
        return (y1, y2)
    else:
        return (z1, z2)
#Координаты точек
x1, x2 = 1, 12
y1, y2 = -5, 9
z1, z2 = 7, -3
#Использование функции из модуля
result = find_min_angle_point(x1, x2, y1, y2, z1, z2)
print(result)