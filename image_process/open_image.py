from PIL import Image
import numpy as np

def open_image():
    #Opening the image with the path provided. 
    image = Image.open('../image/to_compress.jpg')
    return image


