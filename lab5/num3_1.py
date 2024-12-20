import math
def make_x(a,b,h) -> list:
    res=[a]
    while a+h<=b:
        a=a+h
        res.append(a)
    return res


def sm(formula,formula2,a,b,h, k=0):
    for x in make_x(a,b,h):
        i=1
        s=0
        while (abs(formula(x, i))>=0.0001):
            s+=formula(x,i)
            i+=1
        print(s+k, formula2(x))

def formula1(x,i):
    return math.cos(i*x)/math.factorial(i)

def formula1_test(x):
    return (math.e**math.cos(x))*math.cos(math.sin(x))

def formula2(x, i):
    return (((-1)**i)*math.cos(i*x))/i**2

def formula2_test(x):
    return (x**2-(math.pi**2)/3)/4


print("значение для первой функции:")
sm(formula1, formula1_test, 0.1, 1, 0.1, 1)
print("значение для второй функции:")
sm(formula2, formula2_test, math.pi/5 ,math.pi, math.pi/25)


