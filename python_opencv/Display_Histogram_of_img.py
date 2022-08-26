import cv2
import numpy as numpy
from matplotlib import pyplot as pyplot

img = cv2.imread("lena_copy.jpg",0)
# convert image to gray scale
RGB2GRAY(img)
# show histogram of image using imhist()

imshow(img)
imhist(img)