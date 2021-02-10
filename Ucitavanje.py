import tensorflow
from numpy import genfromtxt
import numpy as np
print("ucitavanje...")

#my_data = np.array([])
data = genfromtxt('train.csv', delimiter=',')
label = []
slika = []
for i in range(data.shape[0]):
    a = [0] * 10
    a[int(data[i][0])] = 1
    label.append(a)
    slika.append(data[i][1:].reshape(28,28,1))

label = np.array(label)
slika = np.array(slika)

np.save("label_train.obj", label)
np.save("slika_train.obj", slika)

print(slika[0])

