import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy

image = plt.imread("image.jpg")

width = image.shape[0]
height = image.shape[1]

image = image.reshape(width * height, 3)

kmeans = KMeans(n_clusters=4).fit(image)
labels = kmeans.predict(image)
clusters = kmeans.cluster_centers_

imagesCustom = numpy.zeros_like(image)

for i in range(len(imagesCustom)):
    imagesCustom[i] = clusters[labels[i]]

plt.imshow(imagesCustom.reshape(width, height, 3))
plt.show()