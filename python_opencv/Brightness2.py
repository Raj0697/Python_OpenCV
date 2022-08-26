import numpy as np
import cv2
image = cv2.imread("opencv-logo.png",0)
print(image)

height = image.shape[0]
width = image.shape[1]

brightness = 200

for i in np.arange(height):
    for j in np.arange(width):
        a = image.item(i,j)
        b = a + brightness
        if b > 255:
            b = 255
        image.itemset((i,j),b)
cv2.imshow("img",image)
cv2.waitKey(0)
cv2.destroyAllWindows()