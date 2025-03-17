import random
import numpy as np
import matplotlib.pyplot as plt


def generate_data(x_min, x_max, y_min, y_max, count, label):
    x = [[random.uniform(x_min, x_max), random.uniform(y_min, y_max)] for _ in range(count)]
    y = [label] * count
    return x, y


def train_test_split(x, y, p=0.8):
    data = []
    for i in range(len(x)):
        data.append((x[i], y[i]))
    
    random.shuffle(data)
    train_size = int(len(data) * p)
    train_data, test_data = data[:train_size], data[train_size:]
    
    x_train, y_train = [], []
    for point, label in train_data:
        x_train.append(point)
        y_train.append(label)
    
    x_test, y_test = [], []
    for point, label in test_data:
        x_test.append(point)
        y_test.append(label)
    
    return x_train, x_test, y_train, y_test


def euclidean_distance(p1, p2):
    return np.sqrt(sum((np.array(p1) - np.array(p2)) ** 2))


def fit(x_train, y_train, x_test, k=3):
    y_predict = []
    for test_point in x_test:
        distances = []
        for i in range(len(x_train)):
            train_point = x_train[i]
            label = y_train[i]
            distance = euclidean_distance(test_point, train_point)
            distances.append((distance, label))
        
        distances.sort(key=lambda x: x[0])
        
        k_nearest = []
        for i in range(min(k, len(distances))):
            k_nearest.append(distances[i][1])
        
        label_counts = {}
        for label in k_nearest:
            if label in label_counts:
                label_counts[label] += 1
            else:
                label_counts[label] = 1
        
        most_common = None
        max_count = 0
        for label, count in label_counts.items():
            if count > max_count:
                max_count = count
                most_common = label
                
        y_predict.append(most_common)
    return y_predict


def compute_accuracy(y_test, y_predict):
    correct = 0
    for i in range(len(y_test)):
        if y_test[i] == y_predict[i]:
            correct += 1
    return correct / len(y_test)


x_min1, x_max1, y_min1, y_max1 = 3, 8, 3, 8
x_min2, x_max2, y_min2, y_max2 = 5, 10, 5, 10
points_count1, points_count2 = 30, 30

x1, y1 = generate_data(x_min1, x_max1, y_min1, y_max1, points_count1, 0)
x2, y2 = generate_data(x_min2, x_max2, y_min2, y_max2, points_count2, 1)

x = x1 + x2
y = y1 + y2

x_train, x_test, y_train, y_test = train_test_split(x, y, p=0.8)

y_predict = fit(x_train, y_train, x_test, k=3)

accuracy = compute_accuracy(y_test, y_predict)
print(f"Accuracy: {accuracy:.3f}")

plt.figure(figsize=(8, 6))

for i in range(len(x_train)):
    point = x_train[i]
    label = y_train[i]
    plt.scatter(point[0], point[1], c='blue', marker='o' if label == 0 else 'x',
                label='' if 'Train' not in plt.gca().get_legend_handles_labels()[1] else "")

for i in range(len(x_test)):
    point = x_test[i]
    label = y_test[i]
    pred = y_predict[i]
    color = 'yellow' if label == pred else 'red'
    marker = 'o' if label == 0 else 'x'
    plt.scatter(point[0], point[1], c=color, marker=marker)

plt.legend()
plt.show()