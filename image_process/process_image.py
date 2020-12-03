import sys
import random
import math
import numpy as np
from PIL import Image

def find_numpy_arrays(image):
    #Representing the image chosen in the form of a numpy array
    numpy_array = np.asarray(image)

    #Finding the RGB components of the image
    rgb = Image.Image.split(image)
    r = np.asarray(rgb[0])
    g = np.asarray(rgb[1])
    b = np.asarray(rgb[2])

    return [numpy_array,r,g,b]

def rgb_to_grayscale(rgb):    #Converting RGB image to grayscale. (Not necessary for compression)
    grayscale = 0.2989 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    return grayscale

def find_freq(numpy_array):
    count_dict = {}
    #Iterating through all elements and finding the number of occurrences of each element.
    for i in range(0, len(numpy_array)):
        for j in range(0, len(numpy_array[i])):
            element = numpy_array[i][j]
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1
    return count_dict

#Function to find length of stored bits
def find_length_of_stored_bits(numpy_array):
    length = numpy_array.shape[0]*numpy_array.shape[1]*numpy_array.shape[2]*8
    return length