import cv2
original = cv2.imread('yashwardhan.jpeg')
original_red = cv2.imread('yashwardhan.jpeg')
original_green = cv2.imread('yashwardhan.jpeg')
original_blue = cv2.imread('yashwardhan.jpeg')

original_blue[:,:,1],original_blue[:,:,2] = 0,0
original_green[:,:,0],original_green[:,:,2] = 0,0           
original_red[:,:],original_red[:,:] = 0,0

cv2.imwrite("RED.png",original_red)
cv2.imwrite("GREEN.png",original_green)
cv2.imwrite("BLUE.png",original_blue)
