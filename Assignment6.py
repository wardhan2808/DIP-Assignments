# BT19ECE004 YASHWARDHAN PRATAP SINGH
# Assignment 6:
# Contrast Manipulation on an Image

# Importing required libraries
import math                                               
import numpy as np
import cv2
#declaring path of image
path = r"C:\Users\yashw\Desktop\images\yashwardhan.jpeg" 
#Reading the image
image = cv2.imread(path)                                   
m,n,v = image.shape  
Increased_contrast = np.zeros(image.shape, image.dtype)
Decreased_contrast = np.zeros(image.shape, image.dtype)
# Simple contrast control for High Contrast
alpha_1 = 1.6 
# Simple contrast control for Low Contrast
alpha_2 = 0.7 
# Simple brightness control
beta = 0    

for y in range(image.shape[0]):
    for x in range(image.shape[1]): 
        for c in range(image.shape[2]):
            Decreased_contrast[y,x,c] = np.clip(alpha_2*image[y,x,c] + beta, 0, 255) 
            Increased_contrast[y,x,c] = np.clip(alpha_1*image[y,x,c] + beta, 0, 255)

#Dispalying Images
cv2.imshow("Original Image",image)
cv2.imshow("Contrast Increased Image", Increased_contrast)
cv2.imshow("Contrast Decreased Image", Decreased_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
