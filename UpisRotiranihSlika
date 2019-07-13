import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
from random import randrange
rows = 28
cols = 28
centerX = 14
centerY = 14
data = genfromtxt('train.csv',delimiter = ',')
data = data[1:]
label = []
slika = []
for i in range(data.shape[0]):
    label.append(data[i][0])
    slika.append(data[i][1:].reshape(28,28,1))

for i in range(data.shape[0]):
    omega = randrange(-45,45)
    omega *= (np.pi/180)

a = [[]]
for i in range(rows):
    for j in range(cols):
        a[i].append(0)
    a.append([])

f = open("train.csv","a")

for k in range(data.shape[0]):
    for i in range(rows):
        for j in range(cols):
            jprim = int(centerX - (centerX - j) * np.cos(omega) - (centerY - i) * np.sin(omega))
            iprim = int(centerY + (centerX - j) * np.sin(omega) - (centerY - i) * np.cos(omega) )
            if(0<=iprim<rows and 0<=jprim<cols):
                a[iprim][jprim] = data[k][i][j]
    f.write(str(label[k]) + ",")
    for ni in range(28):
        for nj in range(28):
            f.write(str(a[i][j]) +',')
    f.write('\n')

    


