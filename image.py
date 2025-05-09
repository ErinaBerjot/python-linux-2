import os
import numpy as np
from skimage.io import imread, imsave
from skimage.color import rgb2gray

def process(directoryName):
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(directoryName):
        if not (filename.endswith(".jpg") or filename.endswith(".png")):
            continue

        filenamestr = filename.split('.')[0]
        output_path = os.path.join(output_dir, f"{filenamestr}_modified.jpeg")

        if os.path.exists(output_path):
            continue  # Skip already processed images

        img = imread(os.path.join(directoryName, filename))
        img_new = rgb2gray(img)

        # Save grayscale image (no GUI rendering to avoid memory/CPU load)
        imsave(output_path, (img_new * 255).astype(np.uint8))
