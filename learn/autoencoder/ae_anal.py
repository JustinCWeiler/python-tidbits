#!/home/justin/.venv/learn/bin/python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from keras.models import load_model
from keras.datasets import mnist

num = 5

(x1, _), (x2, _) = mnist.load_data()
x = np.concatenate([x1, x2]).reshape([-1, 28, 28, 1])/255

ae = load_model('ae.h5')
enc = ae.get_layer(index=0)
dec = ae.get_layer(index=1)

encoded = enc.predict(x)

pca = PCA()
pca.fit(encoded)

while True:
    rand = np.random.normal(0, pca.explained_variance_, size=[num, pca.n_components_])

    x_in = pca.inverse_transform(rand)
    x_out = dec.predict(x_in).reshape([-1, 28, 28])

    for i in range(num):
        plt.subplot(1, num, i+1)
        plt.imshow(x_out[i])
    plt.show()
