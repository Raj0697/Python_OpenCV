import cv2
cv2.imread("lena.jpg",1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()