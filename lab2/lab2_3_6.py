'''В компьютер по очереди вводятся координаты п точек. Опре-
делить, сколько из них принадлежит фигуре, ограниченной осью аб-
сцисс и аркой синусоиды, построенной для аргумента от 0 до π'''


#func
import math
PI = 3.14159265
def dot_in_figure(lst:list)-> int:
    res = 0
    for dot in lst:
        x = dot[0]
        y = dot[1]
        if 0<=x<=PI and 0<=y<=math.sin(x):
            res+=1
    return res


#tests
lst1 = [
    [-1, 1],
    [0.3, 0.001],
    [0, 15],
    [1.5, 0.89],
] # output 2

lst2 = [
    [-2, 0],
    [4, 9]
]  # otput 0 

print("Тест 1:", dot_in_figure(lst1))
print("Тест 2", dot_in_figure(lst2))


#input
print("Вводите координаты каждой точки с новой строки, Координаты одной точке вводятся в одной строке, через пробел, первое число координата x, вторая y")
print("Пример:\n 3 7\n-4 9")
print("Чтобы выйти из программы достаточно ввести НЕ число")
lst = []
while True:
    try:
        dot = list(map(float, input().split()))
        lst.append(dot)
    except:
        break

print(dot_in_figure(lst))