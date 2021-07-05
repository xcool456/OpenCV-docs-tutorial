import numpy as np
import cv2 as cv

def nothing(x):
    pass

drawing = False # true if mouse is pressed
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img,(x,y),5,brush_color,-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

img = np.zeros((300,512,3), np.uint8)
img[:] = (255,255,255)
cv.namedWindow('image')

cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    brush_color = [b,g,r]
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()