import numpy as np
import cv2

# create black canvas of size 600x600
img = np.zeros((600, 600, 3), dtype=np.uint8)
# intialize values in unusable states
preview = None
initialPoint = (-1, -1)

# mouse callback


def drawLine(event, x, y, flags, param):
    global initialPoint, img, preview
    if event == cv2.EVENT_LBUTTONDOWN:
        # new initial point and preview is now a copy of the original image
        initialPoint = (x, y)
        preview = img.copy()
        # this will be a point at this point in time
        cv2.line(preview, initialPoint, (x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if preview is not None:
            # copy the original image again a redraw the new line
            preview = img.copy()
            cv2.line(preview, initialPoint, (x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        # if we are drawing, preview is not None and since we finish, draw the final line in the image
        if preview is not None:
            preview = None
            cv2.line(img, initialPoint, (x, y), (255, 0, 0), 1)


# set the named window and callback
cv2.namedWindow("image")
cv2.setMouseCallback("image", drawLine)

while (True):
    # if we are drawing show preview, otherwise the image
    if preview is None:
        cv2.imshow('image', img)
    else:
        cv2.imshow('image', preview)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
