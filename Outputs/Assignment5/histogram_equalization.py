from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#read image
img = mpimg.imread('test.jpg')

#obtain the red, green and blue colour spaces separately
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]

x = 0.2989 * R + 0.5870 * G + 0.1140 * B

plt.imshow(x, cmap='gray')
plt.show()

for i in range(410):
    for j in range(728):
        x[i,j] = round(x[i,j])


his = [0] * 256 
#obtain the histogram
for i in range(410):
    for j in range(728):
        y = int(x[i,j])
        his[y] = his[y] + 1 


p = [0] * 256
for i in range(256):
    p[i] = his[i]/(410*728)


cdf = [0] * 256
for i in range(256):
    for j in range(1+i):
        cdf[i] = cdf[i] + his[j];


cdf_min = cdf[0];        
for i in range(256):
   if(cdf[i] < cdf_min):    
       cdf_min = cdf[i];
       


h = [0] * 256
for i in range(256):
    h[i] = round(((cdf[i]-cdf_min)/((410*728)-cdf_min))*255)


len_his=len(his)
plt.title("Original Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixel Frequency")
plt.plot(range(len_his), his, color ="black")
plt.show()

len_h=len(h)
plt.title("Equalized Values")
plt.xlabel("Original Pixel Intensity")
plt.ylabel("Equalized Pixel Intensity")
plt.plot(range(len_h), h, color ="black")
plt.show()

y=x
for i in range(410):
    for j in range(728):
        for k in range(256):
            if x[i,j] == k:
                y[i,j] = h[k]
                
plt.imshow(y, cmap='gray')
plt.show()
