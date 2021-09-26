import cv2
import numpy as np
import matplotlib.pyplot as plt

def loadImg():
    img = cv2.imread('./Data/bricks.jpg').astype(np.float32)/255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def displayImg(img):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()


img = loadImg()

# Gamma Correction:
gamma = 1/4
result = np.power(img,gamma)
# print(result)
displayImg(result)

# Bluring by 2d filter
img = loadImg()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text="briks",org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
displayImg(img)
kernel = np.ones(shape=(5,5),dtype=np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
displayImg(dst)

# same concept with blut blutin kernal
img = loadImg()
cv2.putText(img, text="briks",org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
dst = cv2.blur(img,(9,9))
displayImg(dst)

#  Guassian and mediem bluring (mean)
img = loadImg()
cv2.putText(img, text="briks",org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
dst = cv2.GaussianBlur(img,(5,5),10)
displayImg(dst)

# Median bluring removing noise to see more details 
img = loadImg()
cv2.putText(img, text="briks",org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
dst = cv2.medianBlur(img, 5)
displayImg(dst)

#  Real example for removing noise with median Bluring

img = cv2.imread('./Data/sammy.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
noiseImg = cv2.imread('./Data/sammy_noise.jpg')
noiseImg = cv2.cvtColor(noiseImg, cv2.COLOR_BGR2RGB)
displayImg(noiseImg)

noiseLess = cv2.medianBlur(noiseImg,5)
displayImg(noiseLess)

#  Bilateral filter also for removing noise 

img = loadImg()
cv2.putText(img, text="briks",org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
dst = cv2.bilateralFilter(img,9,75,75)
displayImg(dst)