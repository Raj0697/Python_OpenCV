import cv2

print(cv2.__version__)

img = cv2.imread('lena.jpg', -1)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)    

print(img)
print(img)
cv2.imshow("image",img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.jpg', img)
    cv2.destroyAllWindows()