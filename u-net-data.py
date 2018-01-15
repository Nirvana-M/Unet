from libtiff import *

imgstack = TIFF3D.read_image('C1_Target_2-2.tif')
for i in range(imgstack.shape[0]):
    savepath = '/deform/tarin/' + str(i) + '.tif'
    img = TIFF.open(savepath, 'w')
    img.write_image(imgstack[i])