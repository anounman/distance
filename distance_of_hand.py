import cv2
import model.hand as hand
import numpy as np
import math

camera = cv2.VideoCapture(0)
detector = hand.HandDetection(detectionCon=0.75)


#data 
a , b , c = [ 2.01978349e-03, -9.88845583e-01,  1.40539209e+02]

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

while 1:
    sucess , img = camera.read()
    img = detector.findHand(img , draw=False)
    lmlist = detector.findPosition(img , draw=False)
    if lmlist:
        x1 = lmlist[5]
        x2  = lmlist[17]
        distance = int(math.sqrt((x1[2]-x2[2])**2 + (x1[1]-x2[1])**2))
        distanceCM = int(a*distance**2 + b*distance + c)
        print(distanceCM)
        cv2.putText(img, str(distanceCM) + "cm", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('img', img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
