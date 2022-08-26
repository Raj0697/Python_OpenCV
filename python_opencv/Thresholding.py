import cv2
import numpy as numpy
from matplotlib import pyplot as pyplot

img = cv2.imread("lena_copy.jpg",0)

ret,thresh1 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original image','BINARY','BINARY INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    # To plot multiple images ,  I have used pyplot.subplot().
    pyplot.subplot(2,3,i+1),pyplot.imshow(images[i],'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]),pyplot.yticks([])

pyplot.show()