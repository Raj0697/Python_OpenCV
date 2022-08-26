import numpy as numpy
import cv2 as cv

img = cv.imread("lena.jpg", 0)

alpha = 5
beta = 10

result = cv.addWeighted(img, alpha, numpy.zeros(img.shape, img.dtype), 0, beta)


cv.imwrite("lena/brightness.jpg", result)

cv.imshow('image',result)
cv.waitKey(0)
cv.destroyAllWindows()