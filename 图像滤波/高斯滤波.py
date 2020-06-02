__author__ = 'Sunny Han'
import numpy as np
import cv2

im1 = cv2.imread("../img/4.png",0)
cv2.imshow("orig",im1)


# 调用OpenCV中的高斯模糊API
im_gaussianblur1 = cv2.GaussianBlur(im1,(5,5),0)
cv2.imshow('gaussian_blur_1',im_gaussianblur1)

cv2.waitKey()
cv2.destroyAllWindows()