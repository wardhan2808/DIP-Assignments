import math                                
import numpy as np
import cv2

I1 = np.zeros((512,512),np.uint8)        
I2 = np.zeros((512,512),np.uint8)

I1 = cv2.circle(I1,(235,250),80,(255,255),-1)            
I2 = cv2.rectangle(I2,(100,300),(330,190),(255,255,255),-1)          


cv2.imshow("Image with white rectangle at center",I2)
cv2.waitKey(0)
cv2.imshow("Image with white circle at center",I1)
cv2.waitKey(0)


cv2.imshow("AND operation on images",cv2.bitwise_and(I1,I2))
cv2.waitKey(0)
cv2.imshow("OR operation on images",cv2.bitwise_or(I1,I2))
cv2.waitKey(0)

cv2.imshow("NAND operation on images",cv2.bitwise_not(cv2.bitwise_and(I1,I2)))
cv2.waitKey(0)
cv2.imshow("NOR operation on images",cv2.bitwise_not(cv2.bitwise_or(I1,I2)))
cv2.waitKey(0)

cv2.imshow("EXOR operation on images",cv2.bitwise_xor(I1,I2))
cv2.waitKey(0)
cv2.imshow("EXNOR operation on images",cv2.bitwise_not(cv2.xor(I1,I2)))
cv2.waitKey(0)
