from display import display, blank_image 
from tile_horizontally import tile_horizontally
import skimage

repeated_image = skimage.io.imread('images/coin.png')

img = blank_image(shape=(450, 800, 4))
img = tile_horizontally(img, repeated_image, (10, 10), 6, shift=130)
img = tile_horizontally(img, repeated_image, (10 + 150, 10), 5, shift=150)
img = tile_horizontally(img, repeated_image, (10 + 2*150, 10), 5, shift=140)
display(img)
