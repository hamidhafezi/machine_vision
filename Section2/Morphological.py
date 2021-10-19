import cv2
import numpy as np 
import matplotlib.pyplot as plt


def loadImg():
    blank_img = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300), fontFace=font,fontScale=5,color=(255,255,255),thickness=25)
    return blank_img

def displayImg(img):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


img = loadImg()
displayImg(img)

# Erosion: romving foreground, and the background is expanded
kernal = np.ones((5,5),dtype=np.uint8)
rst = cv2.erode(img,kernal,iterations=3)
displayImg(rst)

# opening is erosion followed by the dilation
# dialation is opposite of the erosion and add more to foreground
# dilation romove background noise
#  lets add some noise to the image
white_noise = np.random.randint(0,2,(600,600))*255
img = loadImg()
noiseImg = img + white_noise
displayImg(noiseImg)
opening = cv2.morphologyEx(noiseImg, cv2.MORPH_OPEN, kernal)
displayImg(opening)

# sometime we have foreground noise. we use the close method

blackNoise = np.random.randint(0,2,(600,600))*-255
blackNoiseImg = img + blackNoise
blackNoiseImg[blackNoiseImg==-255] = 0
close = cv2.morphologyEx(blackNoiseImg,cv2.MORPH_CLOSE,kernal)
displayImg(blackNoiseImg)
displayImg(close)

# gradiant morphology is difference of the erosion and the dilation of a image
# it is a kind of the edge detction
img = loadImg()
rst = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)
displayImg(rst)