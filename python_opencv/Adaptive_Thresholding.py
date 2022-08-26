import cv2
import numpy as numpy
from matplotlib import pyplot as pyplot

img = cv2.imread("lena_copy.jpg",0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

titles = ['Original image','Global Thresholding (v = 127)','Adaptive Mean Thresholding','Adaptive gaussian thresholding']

images = [img, th1, th2, th3]

for i in range(4):
    pyplot.subplot(2,2,i+1),pyplot.imshow(images[i],'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]),pyplot.yticks([])

pyplot.show()