import numpy as np
import matplotlib.pyplot as plt


# number day student go to school (dataset)
dataSet = [2, 5, 7, 9, 11, 16, 19, 23, 22, 29, 29, 35, 37, 40, 46]
# number point of student (label)
label = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

plt.plot(dataSet, label, 'ro')

# transpose dateset and label
dataSet = np.array([dataSet]).T
label = np.array([label]).T

# create the vector ones
ones = np.ones((dataSet.shape[0], 1), dtype=np.int8)
dataSet = np.concatenate((dataSet, ones), axis=1)

# recipe x = (A^T * A)^-1 * A^T * label
x = np.linalg.inv(dataSet.transpose().dot(dataSet)).dot(dataSet.transpose()).dot(label)

# (y = a * x + b) <=> (y = dataSet * x0 + y0)
a = x[0][0]
b = x[1][0]
x0 = np.array([[1, 46]]).T
y0 = a * x0 + b

# the test model
x_test = input("Enter number day go to school of student: ")
y_test = a * int(x_test) + b

print(f"With {x_test} day go to school ==> The point prediction of student is :", y_test)

# show straight line
plt.title("Linear Regression Model")
plt.plot(x0, y0)
plt.show()