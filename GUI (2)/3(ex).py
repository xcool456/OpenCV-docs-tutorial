import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((256, 256, 3), np.uint8)

#set color to white
img[:] = (255,255,255) 

#green circle
cv.ellipse(img,(65,185),(55,55),0,0,270,(0,255,0),10)

#blue circle
cv.ellipse(img,(190,185),(55,55),315,0,270,255,10)

#red circle
cv.ellipse(img,(128,70),(55,55),135,0,270,(0,0,255),10)

cv.imshow("Display window", img)
k = cv.waitKey(0)