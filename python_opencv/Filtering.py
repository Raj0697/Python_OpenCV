import cv2 as cv
from matplotlib import pyplot as plot

color = cv.imread('apple.jpg',1)
grey = cv.imread('apple.jpg',0)

print(color)
print(grey)

cv.imshow('colorimage',color)
cv.imshow('greyimage',grey)

mean_blur = cv.blur(grey,(5,5))
plot.figure(figsize=(20,8))
plot.imshow(mean_blur)
#cv.imshow('img',mean_blur)

gaussian_blur = cv.GaussianBlur(grey,(101,101),0)
plot.figure(figsize=(20,8))
plot.imshow(gaussian_blur)

median_blur = cv.medianBlur(grey,101)
plot.figure(figsize=(20,8))
plot.imshow(median_blur)

bilateral_blur = cv.bilateralFilter(grey,23,51,51)
plot.figure(figsize=(20,8))
plot.imshow(bilateral_blur)


cv.waitKey(0)
cv.destroyAllWindows()
