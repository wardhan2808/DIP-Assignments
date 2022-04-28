from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#read images
img = mpimg.imread('test.jpg')
img_new = mpimg.imread('test_1.jpg')

#obtain the final image by subtracting the original and edited image
img_final= img - img_new

#display the final result
plt.imshow(img_final)
plt.show()
