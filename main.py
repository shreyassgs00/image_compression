import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'image_process'))
import open_image
import process_image
import huffman_encode
import huffman_tree

def main():
    image = open_image.open_image('./image/to_compress1.jpg')
    image.show()
    numpy_rgb_arrays = process_image.find_numpy_arrays(image)
    
    #Finding the actual length of stored bits which is required to store image data.
    actual_length_of_stored_bits = process_image.find_length_of_stored_bits(numpy_rgb_arrays[0])

    encoded_length = 0
    for i in range(1,4):
        frequencies = process_image.find_freq(numpy_rgb_arrays[i])
        huffman_heap = huffman_tree.create_huffman_tree(frequencies)
        huffman_codes = huffman_encode.huffman_encode(huffman_heap)
        encoded_length = encoded_length + huffman_encode.find_length_of_encoded_bits(huffman_codes, frequencies)

    compression_ratio = huffman_encode.find_compression_ratio(actual_length_of_stored_bits, encoded_length)
    return compression_ratio

if __name__ == '__main__':
    try:
        from PIL import Image
        from operator import itemgetter
        import numpy as np
        import math
        import random
        print('Compression ratio: ' ,main(), '%')
    except:
        print('Dependencies required are not installed.')