import cv2 as cv
import numpy as numpy

img = cv.imread("lena.jpg",0)

equ = cv.equalizeHist(img)
res = numpy.hstack((img,equ)) # stacking image side by side

#cv.imwrite("lena.jpg",res)
cv.imshow("image",res)
cv.waitKey(0)
cv.destroyAllWindows()