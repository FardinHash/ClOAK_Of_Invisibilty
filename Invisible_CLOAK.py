import cv2
import numpy as np
import time

print('Preparing for invisible..........')
cap=cv2.VideoCapture(0)
time.sleep(3)
background=0

for i in range(30):
    ret, background=cap.read()
    background=np.flip(background, axis=1)

    while(cap.isOpened()):
        ret, img=cap.read()

        img=np.flip(img, axis=1)

        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        lower_red=np.array([0,120,70])
        upper_red=np.array([0,255,255])
        mask1=cv2.inRange(hsv,lower_red,upper_red)

        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        mask=mask1+mask2
        mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN, np.ones((5,5),np.uint8))

        img=[np.where(mask==255)]=background[np.where(mask==255)]
        cv2.imshow('Invisible',img)
        k=cv2.waitKey(10)
        if k==27:
            break


