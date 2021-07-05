import numpy as np
import cv2 as cv
img1 = cv.imread('roi.jpg')
img2 = cv.imread('cv.png')
img2 = cv.resize(img2, (150, 150))


# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(img2gray, 240, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

lower_blue = np.array([0, 100, 100])
upper_blue = np.array([255, 255, 255])
mask = cv.inRange(img2,lower_blue,upper_blue)

mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask=mask_inv)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)

img1[0:rows, 0:cols] = dst
cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()
