"""
@Time    : 2017/9/26 0026 22:20
@Author  : Nirvana-YM
@File    : reshape.py
"""

import numpy as np
import cv2
from skimage import exposure
from PIL import Image
import glob
'''
filein:  输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''

def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
    out.save(fileout, type)

def FlipImage(filein, fileout, type):
    fileout = fileout + '_flop.tif'
    img = Image.open(filein)
    out = img.transpose(Image.FLIP_LEFT_RIGHT)  # transpose image
    out.save(fileout, type)

def Contrast(filein, fileout):
    image = cv2.imread(filein, 0)
    gam1 = exposure.adjust_log(image)  # 对数调整
    count = 1

    for i in range(8, 15):
        if i == 10:
            break
        gam = exposure.adjust_gamma(image, 0.1 * i)
        cv2.imwrite(fileout + '_con' + str(count) + '.tif', gam)
        count += 1

    for i in range(4, 6):
        for j in range(6, 10):
            if i == 5 and j == 5:
                break
            img = np.array(image)
            mean = np.mean(img)
            img = img - mean
            img = img * 0.2 * j + mean * 0.2 * i  # 修对比度和亮度
            cv2.imwrite(fileout + '_con' + str(count) + '.tif', img)
            count += 1


if __name__ == "__main__":
    pics = glob.glob("img/measurement/C45/*.png")

    for pic in pics:
        midname = pic[pic.rindex("\\") + 1:]
        onlyname = midname[0:midname.index('.')]

        filein = pic
        fileout = 'img/measurement/prediction/' + midname
        notype_fileout = 'data/testing/label/' + onlyname
        print(onlyname)

        width = 240
        height = 240
        type = 'png'
        ResizeImage(filein, fileout, width, height, type)
        # Contrast(pic, notype_fileout)
        # FlipImage(filein, notype_fileout, type)
