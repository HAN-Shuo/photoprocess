__author__ = 'Sunny Han'
import numpy as np
import cv2

im1 = cv2.imread("../img/4.png",0)
cv2.imshow("orig",im1)


# 调用OpenCV中的均值模糊API
im_meanblur1 = cv2.blur(im1,(10,10))
cv2.imshow('mean_blur_1',im_meanblur1)

cv2.waitKey()
cv2.destroyAllWindows()