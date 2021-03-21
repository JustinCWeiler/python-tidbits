import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape([-1, 28, 28, 1])/255
x_test = x_test.reshape([-1, 28, 28, 1])/255

model = Sequential()
model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(Conv2D(32, (5, 5), activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile('adam', 'sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=256, epochs=10, validation_data=(x_test, y_test))

print(model.evaluate(x_test, y_test, batch_size=32))
