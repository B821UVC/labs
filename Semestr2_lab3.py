import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

points = 100
x_min = -7
x_max = 7
x = np.linspace(x_min, x_max, points)
print(x)
def func(x_list: list, a: float, b: float, c: float):
    y = np.array([a*x**2+b*x+c+random.uniform(-3,3) for x in x_list])
    return y

def y_drawable(x_list: list, a: float, b: float, c: float):
    y_draw = np.array([a*x**2+b*x+c for x in x_list])
    return y_draw
a = 1
b = -5
c = 3
y=func(x, a, b, c)
print(func(x, 10, 4, 12))

def get_da(x_list: list, y_list: list, a: float, b: float, c: float, points: int) -> float:
    lst = []
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        v = (x**2)*(a*x**2+b*x+c - y)
        lst.append(v)
    da = 2/points*sum(lst)
    return da

def get_db(x_list: list, y_list: list, a: float, b: float, c: float, points: int) -> float:

    lst = []
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        v = x*(a*x**2+b*x+c - y)
        lst.append(v)
    db = 2/points*sum(lst)
    return db

def get_dc(x_list: list, y_list: list, a: float, b: float, c: float, points: int) -> float:
    lst = []
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        v = (a*x**2+b*x+c - y)
        lst.append(v)
    dc = 2/points*sum(lst)
    return dc

speed = 0.0001
epochs = 1000
a0=1
b0=2
c0=3
def fit(speed, epochs, a, b, c, points, x, y):
    a_list = [a0]
    b_list = [b0]
    c_list = [c0]
    for i in range(epochs):
        a = a - speed * get_da(x, y, a,b,c, points)
        b = b - speed * get_db(x, y, a,b,c, points)
        c = c - speed * get_dc(x, y, a,b,c, points)
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
    return a_list, b_list, c_list
a_list, b_list, c_list = fit(speed, epochs, a0, b0, c0, points, x, y)


fig, ax = plt.subplots()
ax.scatter(x,y, color="orange")
line, = ax.plot(x, y_drawable(x, a_list[0], b_list[0], c_list[0]))
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
epoch_slider = Slider(
    ax=axfreq,
    label='Эпоха',
    valmin=0,
    valmax=epochs,
    valinit=1,
)

def update(val):
    line.set_ydata(y_drawable(x,  a_list[int(epoch_slider.val)], b_list[int(epoch_slider.val)], c_list[int(epoch_slider.val)] ))
    fig.canvas.draw_idle()
    
epoch_slider.on_changed(update)
plt.show()
