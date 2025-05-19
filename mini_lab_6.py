import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 2*x**3 - 3*x**2 + 5

def df(x):
    return 4*x**3 - 6*x**2 - 6*x

def find_approx_min(f, a=-10, b=10, step=0.1):
    x = np.arange(a, b, step)
    y = f(x)
    return x[np.argmin(y)]

approx_min = find_approx_min(f)
print(f"Примерное значение минимума: x = {approx_min:.2f}")

def gradientDescend(func, diffFunc, x0=3, speed=0.01, epochs=100):
    xList = [x0]
    yList = [func(x0)]
    
    for _ in range(epochs):
        x_new = xList[-1] - speed * diffFunc(xList[-1])
        xList.append(x_new)
        yList.append(func(x_new))
    
    return xList, yList

default_func = lambda x: x**2 + 1
default_diffFunc = lambda x: 2*x

x_values, y_values = gradientDescend(f, df, x0=3, speed=0.01, epochs=100)

print(f"Последнее найденное значение: x = {x_values[-1]:.5f}, y = {y_values[-1]:.5f}")

#Построение графика
def plot_results(f, x_values, y_values, approx_min):
    x_min = min(min(x_values), approx_min)
    x_max = max(max(x_values), approx_min)
    margin = (x_max - x_min) * 0.2
    
    x = np.linspace(x_min - margin, x_max + margin, 400)
    y = f(x)
    
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label='Исходная функция', color='blue')
    
    # Отображение градиентного спуска
    plt.scatter(x_values, y_values, color='red', s=20, label='Точки градиентного спуска')
    
    # Подписываем первую и последнюю точки
    plt.annotate(f'Начальная точка\n({x_values[0]:.2f}, {y_values[0]:.2f})', 
                 xy=(x_values[0], y_values[0]), 
                 xytext=(x_values[0], y_values[0]+0.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    plt.annotate(f'Конечная точка\n({x_values[-1]:.2f}, {y_values[-1]:.2f})',
                 xy=(x_values[-1], y_values[-1]),
                 xytext=(x_values[-1], y_values[-1]+0.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    # Отмечаем приближенный минимум
    plt.axvline(x=approx_min, color='green', linestyle='--', label=f'Примерный минимум x={approx_min:.2f}')
    
    plt.title('Метод градиентного спуска')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_results(f, x_values, y_values, approx_min)

# Проверяем сходимость
converges = abs(x_values[-1] - approx_min) < 0.5
print(f"Результат {'сходится' if converges else 'не сходится'} к искомому минимуму")

#Нахождение граничного значения параметра speed
def find_critical_speed(f, df, x0=3, epochs=100, tolerance=0.1):
    low = 0.001
    high = 1.0
    

    while True:
        test_speed = high
        try:
            x_values, y_values = gradientDescend(f, df, x0=x0, speed=test_speed, epochs=epochs)
            if abs(x_values[-1] - x_values[-2]) > 100:
                break
            else:
                high *= 2
        except OverflowError:
            test_speed = high
            break

    
    mid = (low + high) / 2
    iterations = int(np.log2((high - low)/tolerance)) + 1
    print(iterations)
    for _ in range(iterations):
        mid = (low + high) / 2
        try:
            x_values, y_values = gradientDescend(f, df, x0=x0, speed=mid, epochs=epochs)
            if abs(x_values[-1] - x_values[-2]) > 1: 
                high = mid
            else: 
                low = mid
        except:
            test_speed = high
            break
    
    critical_speed = round(mid, 4)
    print(f"Граничное значение параметра speed: {critical_speed}")
    return critical_speed

critical_speed = find_critical_speed(f, df)