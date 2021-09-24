import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('./Data/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('./Data/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2,(600,600))
x_offset = img1.shape[1]-img2.shape[1]
y_offset = img1.shape[0]-img2.shape[0]
x_end = x_offset+img2.shape[1]
y_end = y_offset+img2.shape[0]

img_large= img1.copy()
large_roi = img1[y_offset:y_end,x_offset:x_end]

img2gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
mask_inv = cv2.bitwise_not(img2gray)

white_background = np.full(img2.shape,255,dtype=np.uint8)
bk = cv2.bitwise_or(white_background,white_background,mask=mask_inv)
print(bk.shape)
fg = cv2.bitwise_or(img2,img2,mask =mask_inv)

plt.imshow(fg)
plt.show()

partly_belended = cv2.addWeighted(large_roi,1,fg,.5,0)
img_large[y_offset:y_end,x_offset:x_end] = partly_belended

plt.imshow(img_large)
plt.show()
