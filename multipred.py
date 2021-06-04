import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt
from tqdm import tqdm_notebook as tqdm
from sklearn.utils import class_weight, shuffle

from keras import applications
from keras import optimizers
from keras.utils import to_categorical
from keras.models import Sequential, Model, load_model
from keras.layers import Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint
from skimage.transform import resize

import numpy as np
from PIL import Image 
from PIL import ImageFilter 
import os 
from skimage.transform import resize
import numpy as np

def cool(my_image):
    
    #my_image='download.jpg'
    fname = "media/"+my_image
    my_image = Image.open(fname) 
    my_image=np.asarray(my_image)
    my_image_resized = resize(my_image, (32,32,3))
    model = load_model('my_cifar10_model.h5')
    probabilities = model.predict(np.array( [my_image_resized,] ))
    number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    index = np.argsort(probabilities[0,:])
    return (number_to_class[index[9]],probabilities[0,index[9]])
##    print("Most likely class:", number_to_class[index[9]], "-- Probability:", probabilities[0,index[9]])
##    print("Second most likely class:", number_to_class[index[8]], "-- Probability:", probabilities[0,index[8]])
##    print("Third most likely class:", number_to_class[index[7]], "-- Probability:", probabilities[0,index[7]])
##    print("Fourth most likely class:", number_to_class[index[6]], "-- Probability:", probabilities[0,index[6]])
##    print("Fifth most likely class:", number_to_class[index[5]], "-- Probability:", probabilities[0,index[5]])

