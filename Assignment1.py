import math                                               
import numpy as np
import cv2
image = cv2.imread('yashwardhan.jpeg')       
m,n,v = image.shape                                      
gray_image = np.zeros((m,n),np.uint8)                   
binary = np.zeros((m,n),np.uint8)  
added_const = np.zeros((m,n),np.uint8)
print("dimensions of image is {}x{}x{}".format(m,n,v))

Sum = 0
for i in range(m):
    for j in range(n):                            
        for k in range(v):
            Sum = Sum + image[i][j][k]
        gray_image[i][j] = math.floor(Sum/3)
        Sum = 0

cv2.imwrite("gray.png",gray_image)

for x in range(m):
    for y in range(n):
        if gray_image[x][y]%2==0 :
          binary[x][y]=0
        else:
          binary[x][y]=255

cv2.imwrite("binary.png",binary)

for x in range(m):
    for y in range(n):
        k=min(gray_image[x][y]+34,255)
        added_const[x][y]=k

cv2.imwrite("Const.png",added_const)
