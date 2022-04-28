#Assignment -9 Histogram of Oriented Gradients
#BT19ECE004
import cv2
import imutils

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap=cv2.VideoCapture("Shopping Mall - 1887.mp4")

while cap.isOpened():
    ret,image=cap.read()
    if ret:
        #resizing of image
        image=imutils.resize(image,width=min(400,image.shape[1]))

        (rects,weights)=hog.detectMultiScale(image,winStride=(4,4),padding=(8,8),scale=1.05)

        for (x,y,w,h) in rects:

            cv2.rectangle(image,(int(x),int(y)),(int(x+w),int(y+h)),(0,0,255),2)

        cv2.imshow("Output",image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
