#!/home/justin/.venv/learn/bin/python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from keras.datasets import mnist

num = 5
side_x, side_y = 10, 10
num_comp = side_x*side_y

(x1, _), (x2, _) = mnist.load_data()
x = np.concatenate([x1, x2]).reshape([-1, 28*28])/255

pca = PCA(num_comp)
space = pca.fit_transform(x)
out = pca.inverse_transform(space)

x = x.reshape([-1, 28, 28])
space = space.reshape([-1, side_x, side_y])
out = out.reshape([-1, 28, 28])


while True:
    rand = np.random.randint(0, 70000, num)
    x_rand = [x[i] for i in rand]
    space_rand = [space[i] for i in rand]
    out_rand = [out[i] for i in rand]

    plt.gray()
    for i in range(num):
        plt.subplot(3, num, i+1)
        plt.imshow(x_rand[i])
        plt.subplot(3, num, num + i+1)
        plt.imshow(space_rand[i])
        plt.subplot(3, num, 2*num + i+1)
        plt.imshow(out_rand[i])
    plt.show()

    """
    new_rand = np.random.normal(0, pca.explained_variance_, [num, num_comp])
    new_out = pca.inverse_transform(new_rand)
    new_rand = new_rand.reshape([-1, side_x, side_y])
    new_out = new_out.reshape([-1, 28, 28])

    for i in range(num):
        plt.subplot(2, num, i+1)
        plt.imshow(new_rand[i])
        plt.subplot(2, num, num + i+1)
        plt.imshow(new_out[i])
    plt.show()
    """
