__author__ = 'Sunny Han'
import numpy as np
import cv2

im = cv2.imread("../img/1.jpg",1)
cv2.imshow("orig",im)
# 定义伽马变化函数
def gamma_trans(img,gamma):
    # 先归一化到1，再做伽马计算，在还原到【0,255】
    gamma_list = [np.power(x/255.0,gamma)*255.0 for x in range(256)]
    # 将列表转化为np.array，并指定类型为uint8
    gamma_table = np.round(np.array(gamma_list)).astype(np.uint8)
    # 使用OpenCV的look up table函数修改图像灰度值
    return cv2.LUT(img,gamma_table)

# 使用伽马值为0.5的变化，实现对暗部的拉升，亮部的压缩
im_gama05 = gamma_trans(im,0.5)
cv2.imshow("gama0.5",im_gama05)

# 使用伽马值为2的变化，实现对暗部的压缩，对亮部的拉升
im_gama2 = gamma_trans(im,2)
cv2.imshow("gama2",im_gama2)

cv2.waitKey()
cv2.destroyAllWindows()