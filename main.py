import sys
import os

sys.path.append('../image_process')
import image

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