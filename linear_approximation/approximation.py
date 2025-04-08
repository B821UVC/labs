import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
N = 15
points = [[x+0.2*random.randint(1,3), x*random.uniform(2.4, 3.8)] for x in range(0, N) ]  #create noise

k=6  #absolutely random
b=10

ka, kb = 0.001, 0.001


def f(k, b, x):
    return k*x+b

def new_y_lst(k, b, points):
    return [f(k, b, point[0]) for point in points]

def split_points(points):
    return [point[0] for point in points], [point[1] for point in points]

def new_k_b(k, b, points, ka, kb, N):
    #MSE = (1/N)*sum([ (point[1]-(k*point[0]+b))**2 for point in points])
    dk = -(2/N)*sum([point[0]*(point[1]-(k*point[0]+b)) for point in points])
    db = -(2/N)*sum([(point[1]-(k*point[0]+b)) for point in points])
    return k-ka*dk, b-kb*db, dk, db



dk=10
db=10
epoch=0
k_list, b_list = [], []
while dk+db>10:
    print(dk, db)
    k, b, dk, db = new_k_b(k, b, points, ka, kb, N)
    k_list.append(k)
    b_list.append(b)
    epoch+=1


x_p, y_p = split_points(points)
#plt.scatter(x_p, y_p)
fig, ax = plt.subplots()
y_p_calc = [f(k,b, x_p[i]) for i in range(N)]
line, = ax.plot(x_p, y_p_calc, lw=2)
ax.scatter(x_p, y_p)
fig.subplots_adjust(left=0.25, bottom=0.25)

axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
n_slider = Slider(
    ax=axfreq,
    label='N stage',
    valmin=1,
    valmax=epoch,
    valinit=1,
)

def update(val):
    num = int(n_slider.val)-1
    line.set_ydata( new_y_lst(k_list[num], b_list[num], points))
    fig.canvas.draw_idle()

n_slider.on_changed(update)
print(epoch)
plt.show()