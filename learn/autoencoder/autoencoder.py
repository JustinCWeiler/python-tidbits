#!/home/justin/.venv/learn/bin/python
import matplotlib.pyplot as plt
import numpy as np

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Reshape
from keras.layers import Conv2D, Conv2DTranspose, MaxPooling2D, UpSampling2D


num_samples = 5


(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train/255
x_test = x_test/255
x_train = np.concatenate([x_train, x_test]).reshape([-1, 28, 28, 1])


encoder = Sequential()
encoder.add(Conv2D(4, 3, padding='same', activation='relu'))
encoder.add(MaxPooling2D())
encoder.add(Conv2D(8, 3, padding='same', activation='relu'))
encoder.add(MaxPooling2D())
encoder.add(Conv2D(16, 3, padding='same', activation='relu'))
encoder.add(Flatten())
encoder.add(Dense(200, activation='relu'))

decoder = Sequential()
decoder.add(Dense(7*7*16, activation='relu', input_dim=200))
decoder.add(Reshape([7, 7, 16]))
decoder.add(UpSampling2D())
decoder.add(Conv2DTranspose(8, 3, padding='same', activation='relu'))
decoder.add(UpSampling2D())
decoder.add(Conv2DTranspose(4, 3, padding='same', activation='relu'))
decoder.add(Conv2DTranspose(1, 3, padding='same', activation='sigmoid'))

autoencoder = Sequential()
autoencoder.add(encoder)
autoencoder.add(decoder)
autoencoder.compile('adadelta', 'binary_crossentropy', metrics=['accuracy'])


autoencoder.fit(x_train, x_train, batch_size=128, epochs=50)
autoencoder.save('ae.h5')


test = np.array([x_train[i] for i in np.random.randint(0, x_train.shape[0], size=num_samples)])
out = autoencoder.predict(test).reshape([-1, 28, 28])

plt.gray()
for i in range(test.shape[0]):
    plt.subplot(2, num_samples, i+1)
    plt.imshow(test[i])
    plt.subplot(2, num_samples, num_samples + i+1)
    plt.imshow(out[i])
plt.show()


test = np.array([x_test[i] for i in np.random.randint(0, x_test.shape[0], size=num_samples)])
out = autoencoder.predict(test).reshape([-1, 28, 28])

plt.gray()
for i in range(test.shape[0]):
    plt.subplot(2, num_samples, i+1)
    plt.imshow(test[i])
    plt.subplot(2, num_samples, num_samples + i+1)
    plt.imshow(out[i])
plt.show()
