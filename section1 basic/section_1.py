import cv2
import numpy as np
import matplotlib.pyplot as plt


# ######## read image via cv2
# img = cv2.imread('./Data/00-puppy.jpg')

# while True:
#     cv2.imshow('Puppy', img)

#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cv2.destroyAllWindows()

blank_img =  np.zeros(shape=(512,512,3),dtype=np.int16)
cv2.rectangle(blank_img,pt1=(384,10),pt2=(500,150),color=(0,256,0),thickness=5)
cv2.circle(blank_img,center=(100,100),radius=50,color=(0,0,256),thickness=-1)
cv2.line(blank_img,pt1=(0,0),pt2=(512,512),color=(256,0,256),thickness=5)
font= cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(blank_img,text="Hello",org=(200,400),fontFace=font,fontScale=2,color=(156,125,156),thickness=2,lineType=cv2.LINE_AA)
vertices = np.array( [[100,300],[200,200],[400,300],[200,400]])
pts= vertices.reshape(-1,1,2)
cv2.polylines(blank_img,pts=[pts],isClosed=True, thickness=3,color=(54,58,56))
plt.imshow(blank_img)

plt.show()