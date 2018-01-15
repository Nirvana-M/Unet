# Implementation of deep learning framework -- Unet, using Keras

The architecture was inspired by [U-Net: Convolutional Networks for Biomedical Image Segmentation](http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/).

---

## Overview

### Data

This experiment is carried out for implementing semiconductor auto-mesurement. The original dataset is confidential, so It was not permitted to be provided in this repo. But for your understanding of the corresponding codes, I still kept the empty data folder.

### Pre-processing

The original semiconductor image is .tiff type, for convinient using, I split the data into different .npy file, for training, validation and testing, respectively.

To do data augumentation, we used separate scripts like contrast.py, reshapre.py and some bash scripts.

### Model

This deep neural network is implemented with Keras functional API, which makes it extremely easy to experiment with different interesting architectures.

Output from the network is a 512*512 which represents mask that should be learned. Sigmoid activation function
makes sure that mask pixels are in \[0, 1\] range.

### Training

The model is trained for 10 epochs.

After 10 epochs, calculated accuracy is about 0.97.

Loss function for the training is basically just a binary crossentropy

---

## How to use

### Dependencies

This tutorial depends on the following libraries:

* Tensorflow
* Keras >= 1.0
* libtiff(optional)

Also, this code should be compatible with Python versions 2.7-3.5.


### Define the model

* Check out ```get_unet()``` in ```unet.py``` to modify the model, optimizer and loss function.

### Train the model and generate masks for test images

* Run ```python unet.py``` to train the model.


After this script finishes, in ```imgs_mask_test.npy``` masks for corresponding images in ```imgs_test.npy```
should be generated.

