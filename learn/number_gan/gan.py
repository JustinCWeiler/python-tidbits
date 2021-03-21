import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Conv2DTranspose, Dropout, BatchNormalization, Flatten, Reshape
from tqdm import tqdm

class GAN:
	def __init__(self):
		generator = Sequential(name='generator')
		generator.add(Dense(64, activation='relu', input_dim=8*8))
		generator.add(Dropout(0.3))
		generator.add(BatchNormalization())
		generator.add(Dense(128, activation='relu'))
		generator.add(Dropout(0.3))
		generator.add(BatchNormalization())
		generator.add(Dense(256, activation='relu'))
		generator.add(Dropout(0.3))
		generator.add(BatchNormalization())
		generator.add(Dense(1024, activation='relu'))
		generator.add(Dropout(0.3))
		generator.add(BatchNormalization())
		generator.add(Dense(36*36, activation='relu'))
		generator.add(Dropout(0.3))
		generator.add(BatchNormalization())
		generator.add(Reshape((36, 36, 1)))
		generator.add(Conv2D(128, 5, activation='relu'))
		generator.add(Dropout(0.3, ))
		generator.add(BatchNormalization())
		generator.add(Conv2D(1, 5, activation='sigmoid'))

		generator.compile('adam', 'binary_crossentropy')
		self.generator = generator


		discriminator = Sequential(name='discriminator')
		discriminator.add(Conv2D(8, 5, activation='relu', input_shape=(28, 28, 1)))
		discriminator.add(Dropout(0.3))
		discriminator.add(Conv2D(16, 5, activation='relu'))
		discriminator.add(Dropout(0.3))
		discriminator.add(Conv2D(32, 5, activation='relu'))
		discriminator.add(Dropout(0.3))
		discriminator.add(Conv2D(64, 5, activation='relu'))
		discriminator.add(Dropout(0.3))
		discriminator.add(Flatten())
		discriminator.add(Dense(128, activation='relu'))
		discriminator.add(Dropout(0.3))
		discriminator.add(Dense(64, activation='relu'))
		discriminator.add(Dropout(0.3))
		discriminator.add(Dense(1, activation='sigmoid'))

		discriminator.compile('adam', 'binary_crossentropy')
		self.discriminator = discriminator

		gan = Sequential()
		discriminator.trainable = False
		gan.add(generator)
		gan.add(discriminator)
		gan.compile('adam', 'binary_crossentropy')
		self.gan = gan
	
	def train(self, real_images, epochs, batch_size=-1):
		if batch_size == -1 or batch_size > real_images.shape[0]:
			batch_size = real_images.shape[0]
		for e in range(1, epochs+1):
			print(f'Epoch {e}/{epochs}')
			for _ in tqdm(range(batch_size)):
				noise = np.random.normal(size=[batch_size, 8*8])
				generated_images = self.generator.predict(noise)

				image_batch = real_images[np.random.randint(0, high=real_images.shape[0], size=batch_size)]

				full_images = np.concatenate([image_batch, generated_images])

				y_dis = np.zeros(2*batch_size)
				y_dis[:batch_size] = 1

				self.discriminator.trainable = True
				self.discriminator.train_on_batch(full_images, y_dis)

				noise = np.random.normal(size=[batch_size, 8*8])
				y_gen = np.ones([batch_size])

				self.discriminator.trainable = False

				self.gan.train_on_batch(noise, y_gen)
	
	def save(self, name='gan.h5'):
		self.gan.save(name)


if __name__ == '__main__':
	gan = GAN()
	gan.generator.summary()
	gan.discriminator.summary()
	gan.gan.summary()