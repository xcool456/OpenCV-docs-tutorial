import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
preview = None
undo = False
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,preview,undo
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_RBUTTONUP:
        undo = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                preview = img.copy()
                cv.rectangle(preview,(ix,iy),(x,y),(255,0,0),1) # A filled rectangle
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        preview = None
        if mode == True:
            if undo == False:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
            undo = False
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    if preview is None or undo:
        cv.imshow('image', img)
    else:
        cv.imshow('image', preview)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()