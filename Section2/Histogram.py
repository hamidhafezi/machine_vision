import cv2
import matplotlib.pyplot as plt
import numpy as np

def imgshow(img,):
    plt.imshow(img,cmap='gray')
    plt.show()


# def readImages():
horse = cv2.imread('./Data/horse.jpg')
show_horse = cv2.cvtColor(horse,cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('./Data/rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow,cv2.COLOR_BGR2RGB)
    
bricks = cv2.imread('./Data/bricks.jpg')
show_bricks = cv2.cvtColor(bricks,cv2.COLOR_BGR2RGB)
# we use images with two chanel order, one for cv2 
# and the other for showing
imgshow(show_bricks)

# Calculation of the histogram using opencv

histValue = cv2.calcHist([horse],channels=[0],
mask=None,histSize=[256],ranges=[0,256])
plt.plot(histValue)
plt.show()
# Note that since the image mostely contain red color it is
# obvious that we see that blue color has zero value in most case

# Now lets plot the histograms of three chanals:
color = ('b', 'g', 'r')

for i,col in enumerate(color):
    histr = cv2.calcHist([bricks], [i], None, [256], [0,256])
    plt.plot(histr,color=col)

plt.show()

# Now lets continue with histogram of regin of interest (ROI)
# To do so we first need to create mask:
  
mask = np.zeros(rainbow.shape[:2],np.uint8)
#  set a part this mask as pure white:
mask[300:400,100:400] = 255
# now we should mask the image using bitwise methods:
masked_rainbow = cv2.bitwise_and(rainbow,rainbow,mask=mask)
imgshow(masked_rainbow)

hist_red = cv2.calcHist([rainbow],channels=[2],histSize=[256],
ranges=[0,256],mask=mask)
plt.plot(hist_red)
plt.show()

# Histogram Equalization is method of contrast adjustment 
# based on the image's histogram.
# roughly speaking the minimum of and image converted to zero
# and the maximum value become 255. This means that we have 
# less shades of gray. In this method cumulative histogram
# may show better visualization. contrast will be increased 
# and cumulative will be linear

gorilla = cv2.imread('./Data/gorilla.jpg',0)
imgshow(gorilla)

histGorilla = cv2.calcHist([gorilla],channels=[0],mask=None
,histSize=[256],ranges=[0,256])
plt.plot(histGorilla)
plt.show()
# now we are going to equalized the gorilla image:
eqGorilla = cv2.equalizeHist(gorilla)
imgshow(eqGorilla)
histeqGorilla = cv2.calcHist([eqGorilla],channels=[0],mask=None
,histSize=[256],ranges=[0,256])
plt.plot(histeqGorilla)
plt.show()

# For colored image first we have to convert rgb to hsv color format.
# Also we should equalize the image for one of the chanals

