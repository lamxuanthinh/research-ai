from sklearn import datasets
import numpy as np
import math
import operator

def accuracy_scores(y_test, y_predict):
    total = len(y_test)
    correct_total = 0

    for i in range(total):
        if y_test[i] == y_predict[i]:
            correct_total += 1

    accuracy = (correct_total/total) * 100
    return accuracy

def calculate_distance(p1, p2):
    dimension = len(p1)
    recipe = 0

    for i in range(dimension):
        recipe += (p1[i] - p2[i])**2

    return math.sqrt(recipe)

def get_k_nearest_neighbors_label(training_x, label_y, k, point):
    distances = []
    nearest_label = []

    for i in range(len(training_x)):
        distance = calculate_distance(training_x[i], point)
        distances.append((distance, label_y[i]))

    distances.sort(key=operator.itemgetter(0))

    for i in range(k):
        nearest_label.append(distances[i][1])

    return nearest_label


def highest_voted(neighbor_label):
    return max(neighbor_label, key=neighbor_label.count)

def predict(training_x, label_y, k, point):
    neighbor_label = get_k_nearest_neighbors_label(training_x, label_y, k, point)
    return highest_voted(neighbor_label)


# prepare data training and testing
iris = datasets.load_iris()
iris_X = iris.data # sepal length, sepal width, petal length, petal width
iris_y = iris.target # 0, 1, 2

random_index = np.arange(len(iris_X))
rng = np.random.default_rng(seed=42)
rng.shuffle(random_index)

iris_X = iris_X[random_index]
iris_y = iris_y[random_index]

x_train = iris_X[:100,:]
x_test = iris_X[100:,:]
y_train = iris_y[:100]
y_test = iris_y[100:]

k = 5
y_predict = []

for p in x_test:
    label = predict(x_train, y_train, k, p)
    y_predict.append(label)

print("Prediction -->", y_predict)
print("Result -->", y_test)

rate_correct = accuracy_scores(y_test, y_predict)
print("Rate correct -->", rate_correct)