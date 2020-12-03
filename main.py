import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'image_process'))
import open_image
import process_image
import huffman_encode
import huffman_tree

def main():
    pass

if __name__ == '__main__':
    try:
        from PIL import Image
        import numpy as np
        import math
        import random

        image = open_image.open_image('./image/to_compress.jpg')
        freq = process_image.process_image(image)
        huffman_tree = huffman_tree.create_huffman_tree(freq)
        huffman_codes = huffman_encode.huffman_encode(huffman_tree)
        print(huffman_codes)
    except:
        print('Dependencies required are not installed.')