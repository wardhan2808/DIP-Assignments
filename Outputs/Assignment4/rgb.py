from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#read image
img = mpimg.imread('test.jpg')

#read the red, green and blue colourspaces differently
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]

#display the images separately
plt.imshow(R, cmap='Reds')
plt.show()

plt.imshow(B, cmap='Blues')
plt.show()

plt.imshow(G, cmap='Greens')
plt.show()
