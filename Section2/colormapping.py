import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./Data/00-puppy.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)

plt.show()
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
plt.imshow(img_hsv)
plt.show()
img_hsl = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
plt.imshow(img_hsl)
plt.show()