import cv2
import numpy as np

img = cv2.imread("plane.jpg",0)
print(img)
height = img.shape[0]
width = img.shape[1]

max_intensity = 255

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        b = max_intensity - a
        img.itemset((i,j),b)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()