import cv2
import numpy as np


# def draw_circle(event,x,y,flags,param):
    
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),radius=20,color=(255,0,0),thickness=-1)
        
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         cv2.circle(img,(x,y),radius=20,color=(0,0,255),thickness=-1)


ix,iy = -1,-1
drawing = False

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x
        iy = y
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,0),thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
cv2.namedWindow(winname='my_drawing')
# cv2.setMouseCallback('my_drawing',draw_circle)
cv2.setMouseCallback('my_drawing',draw_rectangle)




img = np.zeros((512,512,3))

while True:
    cv2.imshow('my_drawing',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()