# -*- coding: utf-8 -*-

#Importing keras libraries and packages.
from keras.models import  Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


#Initialising the CNN
classifier=Sequential()

#Step 1 -Convolution 
# number of filter=32, number of row=3, number of colums=3.
# input shape = dimensions and number of channel( for Colored image=3 and black and white=1).
# Activation is used to get non-linearity.
classifier.add(Convolution2D(32,3,3, input_shape=(64,64,3), activation="relu") )


# Max_pooling
# pool_size=2*2 so we don't loss features
classifier.add(MaxPooling2D(pool_size=(2,2)))

# Flattening: 
#Taking all pooled featured map and put them in a single vector.
classifier.add(Flatten())

# Adding second convoltion layer to increase accuracy.
# we only need featured dectecd.
classifier.add(Convolution2D(32,3,3, activation="relu") )

classifier.add(MaxPooling2D(pool_size=(2,2)))

#Full Connection
#Output_dim= random experiment (common choose to pick power of 2)
classifier.add(Dense(output_dim=128, activation="relu"))

# we have binary outcome Cat or dog. If we have more then two outcome we will self max
# reference to image. CNN_Convolution_2
#output_dim=1  we are going to get predict outcome dog or cat. 
classifier.add(Dense(output_dim=1, activation="sigmoid"))

# complie the CNN 
# Adam is a Algorithm to complie. 
# loss: when two things then binary_crossentropy
# if more than two, then crossentropy
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# Part-2 Fitting the CNN to the images.

from keras.preprocessing.image import ImageDataGenerator
 
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=8000,
        epochs=25,
        validation_data=test_set,
        validation_steps=2000)