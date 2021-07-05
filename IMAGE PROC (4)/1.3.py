import numpy as np
import cv2 as cv
img = cv.imread('cv.png')

color_bgr = np.uint8([[[0, 255, 255]]])
color_hsv = cv.cvtColor(color_bgr, cv.COLOR_BGR2HSV)
print(color_hsv)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([50, 100, 100])
upper_blue = np.array([70, 255, 255])

# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv.bitwise_and(img, img, mask=mask)
cv.imshow('frame', img)
cv.imshow('mask', mask)
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()
