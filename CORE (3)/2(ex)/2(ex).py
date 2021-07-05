import numpy as np
import cv2 as cv
import os
img1 = cv.imread('cv.png')
img2 = cv.imread('roi.jpg')
img2 = cv.resize(img2, (250, 250))
img1 = cv.resize(img1, (250, 250))
directory = r'D:\Шилец\Парк\хлам\Projects\CORE (3)\2(ex)\slide show'
os.chdir(directory)
name = 1
for x in np.arange(0.1, 1, 0.1):
    dst = cv.addWeighted(img1, x, img2, 1-x, 0)
    cv.imwrite(str(name)+".png", dst)
    name += 1
