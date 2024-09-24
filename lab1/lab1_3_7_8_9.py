import math
def make_x(a,b,h) -> list:
    res=[a]
    while a+h<=b:
        a=a+h
        res.append(a)
    return res

def sm(formula,formula2,a,b,h):
    for x in make_x(a,b,h):
        i=0
        s=0
        while (abs(formula(x, i))>=0.0001):
            s+=formula(x,i)
            i+=1
        print(s, formula2(x))



#level 3 №7
def fr_7_1(x,i):
    return ((x)**(2*i))/math.factorial(2*i)
def fr_7_2(x):
    return (math.e**x + math.e**(-x))/2
sm(fr_7_1, fr_7_2, 0.1, 1, 0.05)

#level 3 №8

def fr_8_1(x,i):
    return ((2*x)**(i))/math.factorial(i)
def fr_8_2(x):
    return (math.e**(2*x))
print("№8")
sm(fr_8_1, fr_8_2, 0.1, 1, 0.05)



#level 3 №9
def fr_9_1(x,i):
    return ((-1)**i)*((x**(2*i+1))/(2*i+1))
def fr_9_2(x):
    return (math.atan(x))
print("№9")
sm(fr_9_1, fr_9_2, 0.1, 0.5, 0.05)
