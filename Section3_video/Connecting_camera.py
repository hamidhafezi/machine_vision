import cv2 
import matplotlib.pyplot as plt

# First we get the camera by this command
cap = cv2.VideoCapture(0)

# If we want to get the width and height of the each
# camera frame.

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# in order to record the video you have get from camera:
# first creat a class of the videos writer
# them pass the direction and the name the file
# finally choose a codec based on the your os
# windows: *'DIVX'
# then we need to pass frame rate you want to save from camera
# Also we need width and height of the frame

writer = cv2.VideoWriter('myvideo.mp4',
cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))
# Now lets show the camera frames:
while True:
# read every frame in while loop
    ret,frame = cap.read()
# convert the frame to gray 
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# we can save the videos by this lineL:
    writer.write(frame)
# show the current frame 
    cv2.imshow('Gray',frame)
# end reading the video frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
writer.release()
cv2.destroyAllWindows()