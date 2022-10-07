# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from math import sqrt


xA = int(input('Введите координаты точки А по х: '))
yA = int(input('Введите координаты точки А по y: '))

xB = int(input('Введите координаты точки B по х: '))
yB = int(input('Введите координаты точки B по y: '))

# d = √ (х А – х В) 2 + (у А – у В) 2     формула

distance = sqrt((xA-xB)**2 + (yA - yB)**2)
print(f'A ({xA},{yA}); B ({xB},{yB}) -> {distance: .2f}')