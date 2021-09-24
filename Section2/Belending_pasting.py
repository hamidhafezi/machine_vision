import cv2
from matplotlib import image
import matplotlib.pyplot as plt

img1 = cv2.imread('./Data/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('./Data/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.show()
plt.imshow(img2)
plt.show()

# Belinging with same size
img1_resize = cv2.resize(img1, (1200,1200))
img2_resize = cv2.resize(img2, (1200,1200))

# They become distorted

belnded = cv2.addWeighted(src1=img1_resize, alpha=.7, src2=img2_resize,beta=.3,gamma=0)
plt.imshow(belnded)
plt.show()

# Overlay small imge over large image

img_small = cv2.resize(img2,(600,600))
img_large = img1.copy()
x_offset,y_offset = 0,0
x_end = x_offset+img_small.shape[0]
y_end = y_offset+img_small.shape[1]

img_large[y_offset:y_end,x_offset:x_end] = img_small

plt.imshow(img_large)
plt.show()

# blending small and big image
x_offset = img1.shape[1]-img_small.shape[1]
y_offset = img1.shape[0]-img_small.shape[0]
x_end = x_offset+img_small.shape[1]
y_end = y_offset+img_small.shape[0]
img_large = img1.copy()
large_roi = img1[y_offset:y_end,x_offset:x_end]
partly_belended = cv2.addWeighted(large_roi,.7,img_small,.3,0)
img_large[y_offset:y_end,x_offset:x_end] = partly_belended

plt.imshow(img_large)
plt.show()
