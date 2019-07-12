import numpy as np
import tensorflow
from tensorflow import keras
from keras.models import Sequential

from keras.layers import Conv2D,Dense,MaxPool2D,Flatten ,Input
label = np.load("label_train.obj.npy")
slika = np.load("slika_train.obj.npy")

print(label.shape,slika.shape)

def getModel():
    model = Sequential()
    #model.add(Input(shape = (28,28)))
    model.add(Conv2D(1,(3,3),padding = 'same', input_shape =(28,28,1), activation = 'relu' ) )
    model.add(Conv2D(100,(3,3),padding = "same" , activation = 'relu') ) 
    model.add(MaxPool2D((2,2)  ))
    model.add(Conv2D(100,(3,3),padding = "same", activation = 'relu') ) 
    model.add(MaxPool2D((2,2) ))   
    model.add(Flatten())
    model.add(Dense(5000,activation = 'relu'))
    model.add(Dense(10,activation = 'softmax'))
    model.compile(optimizer = "adam", loss = "categorical_crossentropy" , metrics = ['accuracy'])
    return model

model = getModel()
model.summary()
model.fit(slika,label , epochs = 10 , batch_size = 32 , validation_split = 0.2, shuffle = True  )
model.save_weights("model.h5")
