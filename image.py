import os
import numpy as np
from skimage.io import imread, imshow, imsave
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import helper

def process(directoryName):
    for filename in os.listdir(directoryName):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filenamestr = filename.split('.')[0]
            extension  = filename.split('.')[1]
            img = imread(os.path.join(directoryName, filename))
            img_new = rgb2gray(img)
            fig = plt.figure() 
            ax1 = fig.add_subplot(221)
            imshow(img_new)
            plt.title('Grayscale Format') 
            imsave(os.getcwd() + "/output/" + filenamestr +"-" + helper.generateRandomName() + "_modified.jpeg", (img_new*255).astype(np.uint8))
        else:
            continue