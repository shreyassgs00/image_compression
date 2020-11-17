import sys
import random
import math
import open_image
import numpy as np

def find_numpy(image):
    numpy_array = np.asarray(image)
    return numpy_array

def find_numpy_array():
    image = open_image.open_image()
    numpy_array = find_numpy(image)
    return numpy_array