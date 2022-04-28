from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import operator 

#read images
img_circle = mpimg.imread('circle.jpg')
img_rectangle = mpimg.imread('rectangle.jpg')


#code below is to convert circle image to binary
R, G, B = img_circle[:,:,0], img_circle[:,:,1], img_circle[:,:,2]
binary_circle = (R+G+B)/3
for i in range(500):
    for j in range(500):
        if binary_circle[i,j]>10:
            binary_circle[i,j]=1
        else:
            binary_circle[i,j]=0
plt.imshow(binary_circle, cmap='gray')
plt.show()


#code below is to convert circle image to binary
R, G, B = img_rectangle[:,:,0], img_rectangle[:,:,1], img_rectangle[:,:,2]
binary_rectangle = (R+G+B)/3
for i in range(500):
    for j in range(500):
        if binary_rectangle[i,j]>10:
            binary_rectangle[i,j]=1
        else:
            binary_rectangle[i,j]=0
plt.imshow(binary_rectangle, cmap='gray')
plt.show()


#logical and
img_and = binary_circle.astype(int) & binary_rectangle.astype(int)
plt.imshow(img_and, cmap='gray')
plt.show()

#logical or
img_or = binary_circle.astype(int) | binary_rectangle.astype(int)
plt.imshow(img_or, cmap='gray')
plt.show()

#logical xor
img_xor = binary_circle.astype(int) ^ binary_rectangle.astype(int)
plt.imshow(img_xor, cmap='gray')
plt.show()

#logical nand
img_nand = ~img_and
plt.imshow(img_nand, cmap='gray')
plt.show()

#logical nor
img_nor = ~img_or
plt.imshow(img_nor, cmap='gray')
plt.show()

#logical xnor
img_xnor = ~img_xor
plt.imshow(img_xnor, cmap='gray')
plt.show()