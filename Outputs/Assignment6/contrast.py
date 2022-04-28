from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#read image
img = mpimg.imread('img.jpg')


#Increased contrast
con_inc = img*2

plt.title('Increased Contrast')
plt.imshow(con_inc, cmap='gray')
plt.show()


#decreased contrast
con_dec = img/2

plt.title('Decreased Contrast')
plt.imshow(con_dec, cmap='gray')
plt.show()