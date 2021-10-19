import cv2
import matplotlib.pyplot as plt
import numpy as np

#
def displayImg(img):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()

img = cv2.imread('./Data/sudoku.jpg',0)
displayImg(img)

# Now lets see how we can use sobel operator in opencv

# first x gradiant by sobel:
sobelx = cv2.Sobel(img, cv2.CV_64F, dx=1,dy=0, ksize=5)
displayImg(sobelx)

# and now we calculate y gradiant by sobel:
sobely = cv2.Sobel(img, cv2.CV_64F, dx=0,dy=1, ksize=5)
displayImg(sobely)

# Now lets use laplacian of the image which is the sum of the second derivative
#  of and image
laplacian = cv2.Laplacian(img,ddepth=cv2.CV_64F)
displayImg(laplacian)

# Now for example we want to combine these results of diffent method 
# to achieve better result. lets combine sobelx and sobely:
sobelxy= cv2.addWeighted(src1=sobelx,alpha=.5,src2=sobely,beta=.5,gamma=0)
displayImg(sobelxy)

# we also may want to combine what we have learned before
# like thresholding a image to see whether the numbers can
# be seen better or not:

res,thr = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
displayImg(thr)

# We also can to use the morphological gradiant here:
kernel = np.ones((4,4),np.uint8)
gradiant = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
displayImg(gradiant)
