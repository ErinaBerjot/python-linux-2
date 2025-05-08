import os
import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import helper

def process(directoryName):
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

    for filename in os.listdir(directoryName):
        if not (filename.endswith(".jpg") or filename.endswith(".png")):
            continue  # Skip non-image files

        filenamestr = filename.split('.')[0]
        extension = filename.split('.')[1]

        # Generate unique output path with random name
        output_path = os.path.join(
            output_dir,
            f"{filenamestr}-{helper.generateRandomName()}_modified.jpeg"
        )

        if os.path.exists(output_path):
            continue  # Skip if already processed

        # Load and convert image to grayscale
        img = imread(os.path.join(directoryName, filename))
        img_new = rgb2gray(img)

        # Create and display figure (for saving only, not shown)
        fig = plt.figure()
        plt.imshow(img_new)
        plt.title('Grayscale Format')

        # Save processed image
        imsave(output_path, (img_new * 255).astype(np.uint8))

        # Properly release memory used by the figure
        plt.close(fig)
