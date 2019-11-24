import numpy as np
import matplotlib.pyplot as plt
import skimage, skimage.io

plt.rcParams['figure.dpi'] = 150

def blank_image(shape=(600, 800, 4),
               rgba=(255, 255, 255, 0)):
    "Returns a blank image, of size defined by shape and background color rgb."
    return np.ones(shape, dtype=np.float) * np.array(rgba) / 255.

def display(img, colorbar=False):
    "Displays an image."
    plt.figure(figsize=(10, 10))
    if len(img.shape) == 2:
        i = skimage.io.imshow(img, cmap='gray')
    else:
        i = skimage.io.imshow(img)
    if colorbar:
        plt.colorbar(i, shrink=0.5, label='depth')
    plt.tight_layout()
    plt.show()
