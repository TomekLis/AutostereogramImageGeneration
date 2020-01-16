from display import display, blank_image 
from tile_horizontally import tile_horizontally
from make_pattern import make_pattern
from depth_map import create_circular_depthmap, normalize
from autostereogram_generator import make_autostereogram
import numpy as np
import skimage

repeated_image = skimage.io.imread('images/coin.png')

# img = blank_image(shape=(450, 800, 4))
# img = tile_horizontally(img, repeated_image, (10, 10), 6, shift=130)
# img = tile_horizontally(img, repeated_image, (10 + 150, 10), 5, shift=150)
# img = tile_horizontally(img, repeated_image, (10 + 2*150, 10), 5, shift=140)
# display(img)


pattern = make_pattern(shape=(128, 64))

depthmap = create_circular_depthmap(radius=100)

autostereogram = make_autostereogram(depthmap, pattern)

display(autostereogram)


