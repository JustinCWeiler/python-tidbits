#!/home/justin/.venv/learn/bin/python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from keras.models import load_model
from keras.datasets import mnist

num = 5

(x1, _), (x2, _) = mnist.load_data()
x = np.concatenate([x1, x2]).reshape([-1, 28*28])/255

pca = PCA()
pca.fit(x)

while True:
    rand = np.random.normal(0, pca.explained_variance_, size=[num, pca.n_components_])

    x_out = (pca.inverse_transform(rand)+pca.mean_).reshape([-1, 28, 28])

    for i in range(num):
        plt.subplot(1, num, i+1)
        plt.imshow(x_out[i])
    plt.show()
