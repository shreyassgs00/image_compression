from PIL import Image
import numpy as np

def open_image():
    image = Image.open('../image/to_compress.jpg')
    return image

def find_size(image):
    image_size = image.size
    return image_size


