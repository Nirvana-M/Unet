from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
import os
import glob
import cv2


def load_test_data(npy_path):
    print('-' * 30)
    print('load ground truth images...')
    print('-' * 30)
    imgs_mask_test = np.load(npy_path + "/imgs_mask_test.npy")
    imgs_mask_test = imgs_mask_test.astype('float32')
    imgs_mask_test /= 255
    imgs_mask_test[imgs_mask_test > 0.5] = 1
    imgs_mask_test[imgs_mask_test <= 0.5] = 0
    return imgs_mask_test


def load_pred_data(pred_path):
    print('-' * 30)
    print('load predicted images...')
    print('-' * 30)
    imgs_mask_pred = np.load(pred_path)
    imgs_mask_pred = imgs_mask_pred.astype('float32')

    # imgs_mask_pred /= 255
    imgs_mask_pred[imgs_mask_pred > 0.5] = 1
    imgs_mask_pred[imgs_mask_pred <= 0.5] = 0

    return imgs_mask_pred


#unet_w = 400
#unet_h = 400


def calculate_dice(pred, target):
    comb = pred + target

    L2 = np.sum(comb == 2.0)
    L1 = np.sum(comb == 1.0)
    dice = L2 * 2.0 / (L1 + L2 * 2.0)
    IoU = L2 * 1.0 / (L1 + L2)

    return dice, IoU


if __name__ == "__main__":

    # type1
    #npy_path = "npydata/crop_con_flop"
    #pred_path = "results/imgs_mask_test_crop_con_flop_400.npy"
    # type2
    #npy_path = "npydata/H_crop_con_flop"
    #pred_path = "results/imgs_mask_test_H_crop_con_flop.npy"
    # # type4
    #npy_path = "npydata/RH"
    #pred_path = "results/imgs_mask_test_RH_crop_con_flop.npy"
    # # type5
    #npy_path = "npydata/NRH"
    #pred_path = "results/imgs_mask_test_NRH_crop_con_flop.npy"
    # # the whole
    npy_path = "npydata/NRHRHCyHC"
    pred_path = "results/imgs_mask_test_NRHRHCyHC.npy"

    imgs_mask_test = load_test_data(npy_path)
    imgs_mask_pred = load_pred_data(pred_path)

    dm = np.zeros(len(imgs_mask_test))
    iou = np.zeros(len(imgs_mask_test))

    for i in range(len(imgs_mask_test)):
        imgs_mask_test[i]
        imgs_mask_pred[i]
        dm[i], iou[i] = calculate_dice(imgs_mask_test[i], imgs_mask_pred[i])

    print(dm)
    print("DM mean: " + str(np.mean(dm)))
    print("DM max: " + str(np.amax(dm)))
    print("DM min: " + str(np.amin(dm)))
    print("DM std: " + str(np.std(dm)))

    print("IoU mean: " + str(np.mean(iou)))
    print("IoU max: " + str(np.amax(iou)))
    print("IoU min: " + str(np.amin(iou)))
    print("IoU std: " + str(np.std(iou)))
