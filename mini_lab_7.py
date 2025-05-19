import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def generate_data(n_samples=500, seed=30):
    noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed)
    
    noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05, random_state=seed)
    
    cluster_std = [1.0, 0.5]
    varied = datasets.make_blobs(n_samples=n_samples, cluster_std=cluster_std, random_state=seed, centers=2)
    
    random_state = 170
    x, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state, centers=2)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    x_aniso = np.dot(x, transformation)
    aniso = (x_aniso, y)
    
    blobs = datasets.make_blobs(n_samples=n_samples, random_state=seed, centers=2)
    
    return [noisy_circles, noisy_moons, varied, aniso, blobs]

def split_data(data):
    x_train, x_test, y_train, y_test = train_test_split(
        data[0], data[1], test_size=0.2, random_state=42
    )
    return x_train, x_test, y_train, y_test

# Создание и обучение моделей
def create_models():
    models = [
        ("KNN", KNeighborsClassifier(n_neighbors=3)),
        ("Логистическая регрессия", LogisticRegression(max_iter=200)),
        ("Наивный Байес", GaussianNB())
    ]
    return models

#Создание сетки для построения границы между классами
def create_grid(x):
    temp_x = np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 100)
    temp_y = np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 100)
    xx, yy = np.meshgrid(temp_x, temp_y)
    return xx, yy

def plot_results(models, data_list, titles):
    fig, axes = plt.subplots(5, 3, figsize=(15, 25))
    
    for i, (data, title) in enumerate(zip(data_list, titles)):
        x, y = data
        x_train, x_test, y_train, y_test = split_data((x, y))
        
        xx, yy = create_grid(x)
        
        for j, (name, model) in enumerate(models):
            model.fit(x_train, y_train)
            
            y_pred = model.predict(x_test)
            
            acc = accuracy_score(y_test, y_pred)
            
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            
            ax = axes[i, j]
            ax.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
            
            for k in range(len(x_train)):
                if y_train[k] == 0:
                    ax.scatter(x_train[k, 0], x_train[k, 1], marker='x', c='blue')
                else:
                    ax.scatter(x_train[k, 0], x_train[k, 1], marker='o', c='blue')
            
            for k in range(len(x_test)):
                color = 'green' if y_test[k] == y_pred[k] else 'red'
                if y_test[k] == 0:
                    ax.scatter(x_test[k, 0], x_test[k, 1], marker='x', c=color)
                else:
                    ax.scatter(x_test[k, 0], x_test[k, 1], marker='o', c=color)
            
            ax.set_title(f"{name}\nAccuracy: {acc:.2%}")
            ax.set_xticks([])
            ax.set_yticks([])
            
            if i == 0:
                ax.set_title(f"{name}\nAccuracy: {acc:.2%}", pad=20)
        
        axes[i, 1].set_ylabel(title, rotation=90, fontsize=12)
    
    plt.tight_layout()
    plt.show()

def main():
    data_list = generate_data()
    
    models = create_models()
    
    titles = [
        "Окружности",
        "Луны",
        "Разные кластеры",
        "Анизотропные данные",
        "Пересекающиеся области"
    ]
    
    plot_results(models, data_list, titles)

if __name__ == "__main__":
    main()