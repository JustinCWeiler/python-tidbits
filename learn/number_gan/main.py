import numpy as np
from matplotlib import pyplot as plt
from keras.datasets import mnist

from gan import GAN

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape([-1, 28, 28, 1])/255
x_test = x_test.reshape([-1, 28, 28, 1])/255
x = np.concatenate([x_train, x_test])

gan = GAN()

gan.gan.summary()

gan.train(x, 100, batch_size=100)
gan.save('number_gan/gan.h5')

noise = np.random.normal(size=[10, 8*8])
images = gan.generator.predict(noise)
images = images.reshape([-1, 28, 28])

plt.gray()
for i in range(10):
	plt.subplot(2, 5, i+1)
	plt.imshow(images[i])
plt.show()