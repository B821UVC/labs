import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons, make_circles, make_s_curve
from sklearn.cluster import AffinityPropagation, KMeans, DBSCAN
random.seed(2)  # фиксируем seed=2
methods = random.sample(range(1, 12), 3)
print(methods)

def generate_data_1():
    """Генерация данных с явными кластерами"""
    X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=2)
    return X

def generate_data_2():
    """Генерация данных в форме полумесяцев"""
    X, y = make_moons(n_samples=300, noise=0.05, random_state=2)
    return X

def generate_data_3():
    """Генерация концентрических окружностей"""
    X, y = make_circles(n_samples=300, noise=0.05, factor=0.5, random_state=2)
    return X

def generate_data_4():
    """Генерация данных с неравномерной плотностью"""
    X, y = make_blobs(n_samples=300, centers=1, cluster_std=1.0, random_state=2)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    X = np.dot(X, transformation)
    return X

def generate_data_5():
    """Генерация данных с анизотропными кластерами"""
    X, y = make_blobs(n_samples=300, centers=3, cluster_std=[1.0, 2.5, 0.5], random_state=2)
    return X

def generate_data_6():
    """Генерация данных в форме буквы S"""
    X, t = make_s_curve(300, random_state=2)
    X = X[:, [0, 2]]  # Проецируем на 2D
    X = (X - X.min()) / (X.max() - X.min()) * 10 - 5  # Масштабируем
    return X


def cluster_affinity_propagation(X):
    af = AffinityPropagation(damping=0.75, random_state=2)
    return af.fit_predict(X)

def cluster_kmeans(X):
    kmeans = KMeans(n_clusters=3, random_state=2)
    return kmeans.fit_predict(X)

def cluster_dbscan(X):
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    return dbscan.fit_predict(X)


def plot_results(data_generators, cluster_methods, method_names):
    plt.figure(figsize=(20, 25))
    
    for i, gen in enumerate(data_generators):
        X = gen()
        
        for j, method in enumerate(cluster_methods):
            plt.subplot(len(data_generators), len(cluster_methods), i*len(cluster_methods) + j + 1)
            
            try:
                labels = method(X)
                plt.scatter(X[:, 0], X[:, 1], c=labels, s=10, cmap='viridis')
            except Exception as e:
                plt.scatter(X[:, 0], X[:, 1], s=10, color='red')
                plt.title(f"Error: {str(e)}")
            
            if i == 0:
                plt.title(method_names[j])
            if j == 0:
                plt.ylabel(f'Data {i+1}', rotation=0, ha='right', va='center')
    
    plt.tight_layout()
    plt.show()

# Список генераторов данных
data_generators = [
    generate_data_1,
    generate_data_2,
    generate_data_3,
    generate_data_4,
    generate_data_5,
    generate_data_6
]

# Список методов кластеризации и их названий
cluster_methods = [cluster_affinity_propagation, cluster_kmeans, cluster_dbscan]
method_names = ['Affinity Propagation', 'K-Means', 'DBSCAN']

# Построение графиков
plot_results(data_generators, cluster_methods, method_names)