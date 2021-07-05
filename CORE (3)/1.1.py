import numpy as np
import cv2 as cv
img = cv.imread('roi.jpg')

px = img[100,100]
print( px )
# accessing only blue pixel
blue = img[100,100,0]
print( blue )

img[100:150,100:150] = [255,255,255]
print( img[100,100] )

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

print( img.shape )
print( img.dtype )

ball = img[220:280, 270:330]
print(ball)
img[50:110, 160:220] = ball

# img[:,:,1] = 0
# img[:,:,2] = 0

img = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT)
cv.imshow("Display window", img)
k = cv.waitKey(0)