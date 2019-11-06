import cv2
import numpy as np

img = cv2.imread('/home/y0ch3n/Documents/GitHub/Img-Processing/HW04/test.jpg',0)
# img = cv2.imread('/Users/YoChen/Documents/GitHub/Img-Processing/HW04/test.jpg',0)
print(img[200:250,200:250])
img[200:250,200:250] = img[200:250,200:250]*0
print(img[200:250,200:250])
cv2.imshow('name', img)
cv2.waitKey(0)
cv2.destroyAllWindows()