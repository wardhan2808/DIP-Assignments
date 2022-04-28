from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#read image
img = mpimg.imread('test.jpg')

#obtain the red, green and blue colour spaces separately
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]


red_his = [0] * 256 
#obtain the red histogram
for i in range(410):
    for j in range(728):
      red_his[R[i,j]]= red_his[R[i,j]] + 1 
#plot the histogram
plt.title("Red Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixcel Frequency")
plt.plot(range(256), red_his, color ="red")
plt.show()


blue_his = [0] * 256 
#obtain the blue histogram
for i in range(410):
    for j in range(728):
      blue_his[B[i,j]]= blue_his[B[i,j]] + 1 
#plot the histogram
plt.title("Blue Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixcel Frequency")
plt.plot(range(256), blue_his, color ="blue")
plt.show()


green_his = [0] * 256 
#obtain the green histogram
for i in range(410):
    for j in range(728):
      green_his[G[i,j]]= green_his[G[i,j]] + 1 
#plot the histogram
plt.title("Green Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixcel Frequency")
plt.plot(range(256), green_his, color ="green")
plt.show()
