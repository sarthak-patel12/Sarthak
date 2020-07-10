import numpy as np
import cv2
from keras.datasets import mnist
from keras.models import Sequential,load_model
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical
(X_train,y_train), (X_test,y_test) = mnist.load_data()
training_images = X_train.reshape((60000, 28 , 28,1)).astype('float32') / 255
training_targets = to_categorical(y_train)

test_images = X_test.reshape((10000, 28 , 28,1)).astype('float32') / 255
test_targets = to_categorical(y_test)

input_shape = (training_images.shape[1],)

model =Sequential()
model.add(Conv2D(32,(3,3), activation='relu', input_shape=(28,28,1)))
#model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64, (3,3), activation='relu'))
#model.add(MaxPooling2D((2,2)))
#model.add(Conv2D(64, (3,3), activation='relu'))
#model.add(MaxPooling2D((2,2)))
#model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))
#model.add(Conv2D(64, (3,3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_targets, validation_split=0.3, callbacks=[EarlyStopping(patience=2)], epochs=50)
model.save('Neural_Net')


