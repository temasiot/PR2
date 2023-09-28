from math import pi  # імпорт необхідних елементів
from math import cos
from math import sin
from math import sqrt

a = float(input())  # ввод зміної з клавіатури

z1 = cos(3/8*pi - a/4)**2 - cos(11/8*pi + a/4)**2  # розрахунок z1
z2 = sqrt(2)/2 * sin(a/2)  # розрахунок z2

print('z1=', z1)  # вивід z1
print('z2=', z2)  # вивід z2
