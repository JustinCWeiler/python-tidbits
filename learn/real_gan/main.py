from keras.models import Sequential, Model
from keras.layers import Input, Dense, Reshape, Flatten, Dropout
from keras.layers import BatchNormalization, Activation
from keras.layers.advanced_activations import LeakyReLU
from keras.optimizers import Adam
from keras.datasets import mnist

import matplotlib.pyplot as plt
import sys
import numpy as np


# TODO: possibly use tf.GradientTape with optimizer.apply_gradients to do this but better in the training part


m = Sequential()
m.add(Dense(10))
m.compile('adam', 'mse')


class GAN():
	def __init__(self):
		self.img_rows = 28
		self.img_cols = 28
		self.channels = 1
		self.img_shape = (self.img_rows, self.img_cols, self.channels)
		self.latent_dim = 100


		optimizer = Adam(0.0002, 0.5)  # set learning rate and momentum

		self.discriminator = self.build_discriminator()
		self.discriminator.compile(optimizer, 'binary_crossentropy', metrics=['accuracy'])

		self.generator = self.build_generator()


		z = Input(shape=(self.latent_dim,))
		img = self.generator(z)

		self.discriminator.trainable = False

		validity = self.discriminator(img)

		self.combined = Model(z, validity)
		self.combined.compile(optimizer, 'binary_crossentropy')
	
	def build_generator(self):
		model = Sequential()

		model.add(Dense(256, input_dim=self.latent_dim))
		model.add(LeakyReLU(0.2))
		model.add(BatchNormalization(momentum=0.8))
		model.add(Dense(512))
		model.add(LeakyReLU(0.2))
		model.add(BatchNormalization(momentum=0.8))
		model.add(Dense(1024))
		model.add(LeakyReLU(0.2))
		model.add(BatchNormalization(momentum=0.8))
		model.add(Dense(np.prod(self.img_shape), activation='tanh'))
		model.add(Reshape(self.img_shape))

		noise = Input(shape=(self.latent_dim,))
		img = model(noise)

		return Model(noise, img)
	
	def build_discriminator(self):
		model = Sequential()

		model.add(Flatten(input_shape =self.img_shape))
		model.add(Dense(512))
		model.add(LeakyReLU(0.2))
		model.add(Dense(256))
		model.add(LeakyReLU(0.2))
		model.add(Dense(1, activation='sigmoid'))

		img = Input(shape=self.img_shape)
		validity = model(img)

		return Model(img, validity)
	
	def train(self, epochs, batch_size=32):
		(x_train, _), (x_test, _) = mnist.load_data()
		x_train = x_train.reshape((-1, 28, 28, 1))/255*2 - 1
		x_test = x_test.reshape((-1, 28, 28, 1))/255*2 - 1
		full_imgs = np.concatenate([x_train, x_test])

		valid = np.ones((batch_size, 1))
		fake = np.zeros((batch_size, 1))

		for epoch in range(epochs):
			idx = np.random.randint(0, full_imgs.shape[0], batch_size)
			imgs = full_imgs[idx]

			noise = np.random.normal(size=(batch_size, self.latent_dim))

			gen_imgs = self.generator.predict(noise)

			d_loss_real = self.discriminator.train_on_batch(imgs, valid)
			d_loss_fake = self.discriminator.train_on_batch(gen_imgs, fake)
			d_loss = 0.5*np.add(d_loss_real, d_loss_fake)


			noise = np.random.normal(size=(batch_size, self.latent_dim))

			g_loss = self.combined.train_on_batch(noise, valid)


			print("%d [D loss: %f, acc.: %.2f%%] [G loss: %f]" % (epoch, d_loss[0], 100*d_loss[1], g_loss))


if __name__ == '__main__':
	gan = GAN()
	gan.train(epochs=100000, batch_size=128)
	gan.combined.save('real_gan/real_gan.h5')

	noise = np.random.normal(size=(10, gan.latent_dim))
	imgs = gan.generator.predict(noise)

	plt.gray()
	for i in range(10):
		plt.subplot(2, 5, i+1)
		plt.imshow(imgs[i])
	plt.show()