import matplotlib.pyplot as plt
import glob
import simplejson as json
import numpy as np

logs = glob.glob("log_txt/*.txt")

count = 0
for log in logs:
    with open(log, "r") as f:
        text = f.read()
        print(text)

    # str to dic
    text = text.replace("'", "\"")
    history = json.loads(text)
    
    # list all data in history
    print(history.keys())

    model_name = ['Cropped', 'Crop_Con', 'Crop_Con_Flop']
    plt.plot(history['acc'])
    plt.plot(history['val_acc'])

    # summarize history for accuracy
    if count == 0:
        plt.ylim(0.65, 1)

        x = np.arange(10) + 0.1
        y = np.array(list(history['acc']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b+0.01, round(b, 4), ha='center', va='bottom', fontsize=7)

        x = np.arange(10) + 0.1
        y = np.array(list(history['val_acc']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b-0.01, round(b, 4), ha='center', va='bottom', fontsize=7)
    else:
        plt.ylim(0.95, 1)

        x = np.arange(10) + 0.1
        y = np.array(list(history['acc']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b + 0.001, round(b, 4), ha='center', va='bottom', fontsize=7)

        x = np.arange(10) + 0.1
        y = np.array(list(history['val_acc']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b - 0.001, round(b, 4), ha='center', va='bottom', fontsize=7)
    plt.title('Model Accuracy - ' + model_name[count])
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.tight_layout()
    plt.savefig('result_img/accuracy_' + model_name[count] + '.png')
    # plt.xlim(0, 10)


    plt.show()
    # summarize history for loss
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])

    if count == 0:
        plt.ylim(0.5, 0.7)

        x = np.arange(10) + 0.1
        y = np.array(list(history['loss']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b - 0.007, round(b, 4), ha='center', va='bottom', fontsize=7)

        x = np.arange(10) + 0.1
        y = np.array(list(history['val_loss']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b + 0.003, round(b, 4), ha='center', va='bottom', fontsize=7)

    elif count == 1:
        plt.ylim(0.4, 0.6)

        x = np.arange(10) + 0.1
        y = np.array(list(history['loss']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b - 0.008, round(b, 4), ha='center', va='bottom', fontsize=7)

        x = np.arange(10) + 0.1
        y = np.array(list(history['val_loss']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b + 0.003, round(b, 4), ha='center', va='bottom', fontsize=7)

    elif count == 2:
        plt.ylim(0.25, 0.45)

        x = np.arange(10) + 0.1
        y = np.array(list(history['loss']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b - 0.001, round(b, 4), ha='center', va='bottom', fontsize=7)

        x = np.arange(10) + 0.1
        y = np.array(list(history['val_loss']))
        for a, b in zip(x, y):
            print(a, b)
            plt.text(a, b + 0.001, round(b, 4), ha='center', va='bottom', fontsize=7)

    plt.title('Model Loss - ' + model_name[count])
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.tight_layout()
    plt.savefig('result_img/loss_' + model_name[count] + '.png')
    plt.show()
    count += 1