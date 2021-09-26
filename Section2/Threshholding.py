import cv2
import matplotlib.pyplot as plt

### Basic Thresholding
img= cv2.imread('./Data/rainbow.jpg',0)
plt.imshow(img,cmap='gray')
plt.show()

# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)


plt.imshow(thresh1,cmap='gray')
plt.show()
##################################
####  Cross Word Image  #########
def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')
    plt.show()

img2 = cv2.imread('./Data/crossword.jpg',0)
ret,th1 = cv2.threshold(img2,180,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
blended = cv2.addWeighted(th1,.5,th2,.5,0)
show_pic(blended)
