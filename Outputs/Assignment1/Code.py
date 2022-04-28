from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#read image
img = mpimg.imread('test.jpg')

#obtain the red, blue and green layers
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
imgGray = (R+G+B)/3

#show red layer
plt.imshow(R, cmap='Reds')
plt.show()

#show blue layer
plt.imshow(B, cmap='Blues')
plt.show()

#show green layer
plt.imshow(G, cmap='Greens')
plt.show()

#show grayscale image
plt.imshow(imgGray, cmap='gray')
plt.show()

#loop to convert to binary
#all pixels with value over 10 will be 1 and other zero
binary = (R+G+B)/3
for i in range(4526):
    for j in range(10000):
        if binary[i,j]>10:
            binary[i,j]=1
        else:
            binary[i,j]=0
#display binary image
plt.imshow(binary, cmap='gray')
plt.show()

#add binary and grayscale
img_new = binary + imgGray
plt.imshow(img_new, cmap='gray')
plt.show()

#add 20 to grayscale
gray_20 = 20 + imgGray
plt.imshow(gray_20, cmap='gray')
plt.show()
