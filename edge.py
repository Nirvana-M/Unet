# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:28:15 2017

@author: Cheng Zhong Yao
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('edge_img/testing_t.tif', 0)

ret, img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
edges = cv2.Canny(img, 100, 200)

img1 = cv2.imread('edge_img/testing.tif')
for i in range(0,400):
    for j in range(0,400):
        if(edges[i][j]==255):
            img1[i][j][0]=0
            img1[i][j][1]=0
            img1[i][j][2]=255
            if i != 399 and j != 399:
                img1[i+1][j][0]=0
                img1[i+1][j][1]=0
                img1[i+1][j][2]=255
                img1[i][j+1][0]=0
                img1[i][j+1][1]=0
                img1[i][j+1][2]=255

cv2.imwrite('edge_img/testing.png',img1)
