import cv2
import numpy


image = cv2.imread('aim.png')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('few', image)
cv2.imwrite('gray.bmp', image)
