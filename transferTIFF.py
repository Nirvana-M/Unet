import numpy as np
from PIL import Image

# predict = np.load("results/imgs_mask_test_H_crop_con_flop.npy", 'r')
predict = np.load("results/measurement.npy", 'r')
# actual = np.load("npydata/cy/imgs_mask_test.npy", 'r')

# xb = Image.open("push/a.tif")
# ct = Image.open("push/b.tif")
# xb_t = Image.open("push/7.png")
# ct_t = Image.open("push/2.png")


# index = range(len(predict))
# np.random.shuffle(index)

# predict_shuffle = []
# actual_shuffle = []
# for i in index:
#     predict_shuffle.append(predict[i])
#     actual_shuffle.append(actual[i])
#
print('hh')

count = 0.0
for i in range(len(predict)):
    print(count)
    # pre = predict[i, :]
    # act = actual[i, :]
    # pre = np.array(pre)
    # act = np.array(act)
    # pre = pre.reshape(160000)
    # act = act.reshape(160000)
    # for j in range(len(pre)):
    #     pre[pre > 0.5] = 1.
    #     pre[pre <= 0.5] = 0.
        # act[act > 0.5] = 1.
        # act[act <= 0.5] = 0.
        #
        # if pre[j] == act[j]:
        #     count += 1.0

    item = predict[i, :]
    item = np.array(item)
    item = item*255
    item = item.astype(np.uint8)
    item = item.reshape(400, 400)
    im = Image.fromarray(item)
    im.save('img/measurement/' + str(i) + '.png')

# acc = float(count)
# acc = count/400./400./len(predict)
# print(acc)

