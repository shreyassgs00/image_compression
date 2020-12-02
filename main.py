import sys
import os

sys.path.append('/media/shreyas/DATA/linux_files/image_compression/image_process')
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
    except:
        print('Dependencies required are not installed.')