# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:11:07 2017

@author: Cheng Zhong Yao
"""

import sys
import re
import os
import numpy as np
import cv2
#import matplotlib.pyplot as plt
from skimage import data, exposure, img_as_float


fname = sys.argv[1]
filename = 'data/gan/' + re.split('\/|\.',fname)[-2]
image = cv2.imread(fname,0)
gam1= exposure.adjust_log(image)   #对数调整
#plt.figure('adjust_gamma',figsize=(8,8))

#plt.subplot(121)
#plt.title('origin image')
#plt.imshow(image,plt.cm.gray)
#plt.axis('off')

#plt.subplot(122)
#plt.title('log')
#plt.imshow(gam1,plt.cm.gray)
#plt.axis('off')

#plt.show()
count = 1
for i in range(8,15):
    if i == 10:
        break
    gam = exposure.adjust_gamma(image, 0.1*i)
    cv2.imwrite(filename+'_con'+str(count)+'.tif',gam)
    count += 1

for i in range(4,6):
    for j in range(6,10):
        if i == 5 and j == 5:
            break
        img = np.array(image)
        mean = np.mean(img)
        img = img - mean
        img = img*0.2*j + mean*0.2*i #修对比度和亮度
        #img = img/255.
        #plt.imshow(img,plt.cm.gray)
        #cv2.imwrite(filename+'_mean'+np.str(i)+np.str(j)+'.tif',img)
        cv2.imwrite(filename+'_con'+str(count)+'.tif',img)
        count += 1
