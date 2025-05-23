import matplotlib.pyplot as plt
import numpy as np

r = True
while r:
    print("left border need to be more than 0")
    left, right = int(input("left: ")), int(input("right: "))
    if left < 0:
        continue
    r = False
a, b= int(input("a: ")), int(input("b: "))

x_array = np.linspace(left, right, 200)

def f(a, b, x):
    return a+b*x**(3/2)

y = [f(a,b,x) for x in x_array]

plt.plot(x_array, y)
plt.show()

#num2

with open("a.txt", "r") as f:
    X = [float(x) for x in f.readline().rstrip().split(":")]
    Y = [float(y) for y in f.readline().rstrip().split(":")]

plt.scatter(X, Y)
plt.show()