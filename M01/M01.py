print("\033c")
#import libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

#Tentukan domain diagram cartesian dan rasio lebar tingginya diagram
x= np.linspace(-10,10,1000)
plt.figure(figsize=(4,15))

#Menggambar lingkaran di (0,0)
plt.plot(x, (0.05-x**2)**0.5, '-k')
plt.plot(x, -(0.05-x**2)**0.5, '-k')

#Tentukan persamaan matematika yang diinginkan
y1 = x -x -0
y2 = 0.5*x
y3 = x
y4 = -0.05*x
y5 = -2*x
y6 = -x
y7 = -2*x

plt.plot(x, y1, '-k', label='y1')
plt.plot(x, y2, '-r', label='y2')
plt.plot(x, y3, '-g', label='y3')
plt.plot(x, y4, '-b', label='y4')
plt.plot(x, y5, '-y', label='y5')
plt.plot(x, y6, '-m', label='y6')
plt.plot(x, y7, '-c', label='y7')

plt.legend(loc = 'upper left')
plt.grid()
plt.show()