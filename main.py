# main code of autostereogram project
from display import display, blank_image 
from tile_horizontally import tile_horizontally
from make_pattern import make_pattern
from depth_map import create_circular_depthmap, normalize
import numpy as np
import skimage
# Horizontally Shifted Patterns code
repeated_image = skimage.io.imread('images/coin.png')

img = blank_image(shape=(450, 800, 4))
img = tile_horizontally(img, repeated_image, (10, 10), 6, shift=130)
img = tile_horizontally(img, repeated_image, (10 + 150, 10), 5, shift=150)
img = tile_horizontally(img, repeated_image, (10 + 2*150, 10), 5, shift=140)
display(img)

# Depth map (random dots) code
pattern = make_pattern(shape=(128, 64))

depthmap = create_circular_depthmap(radius=150)

def make_autostereogram(depthmap, pattern, shift_amplitude=0.1, invert=False):
    "Creates an autostereogram from depthmap and pattern."
    depthmap = normalize(depthmap)
    if invert:
        depthmap = 1 - depthmap
    autostereogram = np.zeros_like(depthmap, dtype=pattern.dtype)
    for r in np.arange(autostereogram.shape[0]):
        for c in np.arange(autostereogram.shape[1]):
            if c < pattern.shape[1]:
                autostereogram[r, c] = pattern[r % pattern.shape[0], c]
            else:
                shift = int(depthmap[r, c] * shift_amplitude * pattern.shape[1])
                autostereogram[r, c] = autostereogram[r, c - pattern.shape[1] + shift]
    return autostereogram


autostereogram = make_autostereogram(depthmap, pattern)
display(autostereogram)


