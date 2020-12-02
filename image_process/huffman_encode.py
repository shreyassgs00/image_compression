from process_image import find_numpy_arrays
import huffman_tree
#https://www.programiz.com/dsa/huffman-coding

import numpy as np
import random
import math
from operator import itemgetter

#First, we need to find the frequencies of each element before encoding the same and store them in a dictionary.
def find_freq(numpy_array):
    count_dict = {}
    #Iterating through all elements and finding the number of occurrences of each element.
    for i in range(0,len(numpy_array)):
        for j in range(0,len(numpy_array[i])):
            element = numpy_array[i][j]
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1
    return count_dict

#Sorting the dictionary so that the element with least number of occurrences comes first and so on.
def sort_dict(count_dict):
    sorted_dict = dict(sorted(count_dict.items(), key = itemgetter(1)))
    return sorted_dict






