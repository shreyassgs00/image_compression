import open_image

import sys
import random
import math
import numpy as np
from PIL import Image

def find_numpy_arrays():
    image = open_image.open_image()
    
    #Representing the image chosen in the form of a numpy array
    numpy_array = np.asarray(image)

    #Finding the RGB components of the image
    rgb = Image.Image.split(image)
    r = np.asarray(rgb[0])
    g = np.asarray(rgb[1])
    b = np.asarray(rgb[0])

    return [r,g,b]

def rgb_to_grayscale(rgb):    #Converting RGB image to grayscale. (Not necessary for compression)
    grayscale = 0.2989 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    return grayscale

