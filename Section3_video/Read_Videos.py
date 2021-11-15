import cv2 
import time


cap = cv2.VideoCapture('File path and name')


# When using a cv2 we should check wether we use a right path or not
# otherwise cv2 did not return any error 
if cap.isOpened() ==False:
    print('Error, File not found or wrong codec is used')

while cap.isOpened:
    
    ret, frame = cap.read()
    time.sleep(1/20)
    if ret == True:
        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(10) && oxFF == ord(q):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()


