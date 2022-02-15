#BT19ECE004 YASHWARDHAN PRATAP SINGH
#Assignment-4
#Reading a color image and display its Red, Green and Blue components


import cv2
#declaring path of image
path = r"C:\Users\Desktop\images\yashwardhan.jpeg" 
#Reading the image
original = cv2.imread(path)                                 
original_red = cv2.imread(path)
original_green = cv2.imread(path)
original_blue = cv2.imread(path)

#Converting Images to Red, Green and Blue
#For Blue : Green and Red = 0
original_blue[:,:,1],original_blue[:,:,2] = 0,0  
#For Green : Red and Blue = 0   
original_green[:,:,0],original_green[:,:,2] = 0,0            
#For Red : Blue and Green = 0 
original_red[:,:,0],original_red[:,:,1] = 0,0       

#Dispalying Images
cv2.imshow("Original Image",original)
cv2.waitKey(0)
cv2.imshow("Red Component",original_red)
cv2.waitKey(0)
cv2.imshow("Green Component",original_green)
cv2.waitKey(0)
cv2.imshow("Blue Component",original_blue)
cv2.waitKey(0)
