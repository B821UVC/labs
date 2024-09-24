PI = 3.14
SQRT3 = 1.732
def area_square(r):
    print(f"Площадь квадрата с стороной {r}: {r**2}")
def area_circle(r):
    print(f"Площадь круга с радиусом {r}: {PI*(r**2)}")
def area_triangle(r):
    print(f"Площадь равностороннего треугольника с стороной {r}: {(SQRT3*(r**2))/4}")

def how_to_use():
    print("Программа вычисляет площадь фигур")
    print("первым параметр - вид фигуры")
    print("1 - квадрат\n2 - круг\n3 - равносторонний треугольник")
    print("второй параметр это длина")
    print("Данные вводятся в одну строку через пробел")
    print("Например строка \"1 4\" выведет площадь квадрата с стороной равной 4")

how_to_use()
while True:
    try:
        inp = [int(x) for x in input().split()]
        r, flag = inp[1], inp[0]
        if flag==1:
            area_square(r)    
        elif flag==2:
            area_circle(r)
        elif flag==3:
            area_triangle(r)
    except:
        break