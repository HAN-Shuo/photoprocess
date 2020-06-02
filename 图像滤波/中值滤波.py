__author__ = 'Sunny Han'
import numpy as np
import cv2

im1 = cv2.imread("../img/4.png",0)
cv2.imshow("im1",im1)
im2 = cv2.imread("../img/3.jpg",0)
cv2.imshow("im2",im2)

# 调用OpenCV中的中值模糊API
im_medianblur = cv2.medianBlur(im1,5)
cv2.imshow('median_blur',im_medianblur)

cv2.waitKey()
cv2.destroyAllWindows()