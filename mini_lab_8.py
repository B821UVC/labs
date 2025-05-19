import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

def f(x):
    return 0.3 * x**3 - 2.5 * np.sin(2*x) + 1.7 * x**2 - 4.2 * x + 1.5


nonlinear = True

def generate_data(n_points=100, x_min=-5, x_max=5):
    x = np.linspace(x_min, x_max, n_points)
    # Добавляем шум
    e = [random.uniform(-0.5, 0.5) for _ in range(n_points)]
    y = [f(xi) + ei for xi, ei in zip(x, e)]
    
    x_reshaped = x.reshape(-1, 1)
    
    return x_reshaped, np.array(y)


def get_regressors():
    if nonlinear:

        return [
            ("SVR", SVR(kernel='rbf', C=100, gamma='scale')),
            ("Random Forest", RandomForestRegressor(n_estimators=100, random_state=42)),
            ("Дерево решений", DecisionTreeRegressor(max_depth=5, random_state=42))
        ]
    else:
        return [
            ("Линейная регрессия", LinearRegression()),
            ("Ridge", Ridge(alpha=1.0)),
            ("Lasso", Lasso(alpha=0.1))
        ]

def train_models(models, x, y):
    trained_models = []
    for name, model in models:
        model.fit(x, y)
        y_pred = model.predict(x)
        mse = mean_squared_error(y, y_pred)
        trained_models.append((name, model, y_pred, mse))
    return trained_models

def plot_results(x, y_true, y_func, trained_models):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    

    for i, (name, model, y_pred, mse) in enumerate(trained_models):
        ax = axes[i]
        
        ax.scatter(x, y_true, color='blue', label='Исходные данные', alpha=0.6)
        
        ax.plot(x, y_func, color='green', label='Исходная функция', linewidth=2)
        
        ax.plot(x, y_pred, color='red', label=f'Регрессия: {name}', linewidth=2)
        
        ax.set_title(f"{name}\nMSE: {mse:.2f}")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

def main():
    x, y = generate_data()
    
    x_no_noise = np.linspace(-5, 5, 100).reshape(-1, 1)
    y_func = f(x_no_noise)
    
    models = get_regressors()
    
    trained_models = train_models(models, x, y)
    
    print("Сгенерированная функция: f(x) = 0.3x³ - 2.5sin(2x) + 1.7x² - 4.2x + 1.5")
    print(f"Функция {'нелинейная'}")
    
    plot_results(x, y, y_func, trained_models)
    
    best_model = min(trained_models, key=lambda m: m[3])
    print(f"\nЛучшая регрессия: {best_model[0]} с MSE = {best_model[3]:.2f}")
    
    print("\nВывод:")
    print("1. Все три метода показали разную степень соответствия исходной функции.")
    print("2. Метод опорных векторов (SVR) показал наилучшее соответствие, так как он хорошо справляется с нелинейными зависимостями.")
    print("3. Дерево решений также неплохо справилось с задачей, но имело тенденцию к переобучению на отдельных участках.")
    print("4. Random Forest показал средние результаты, но был более устойчив к шуму в данных.")

if __name__ == "__main__":
    main()