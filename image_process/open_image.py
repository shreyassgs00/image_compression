from PIL import Image

def open_image(image_path):
    #Opening the image with the path provided. 
    image = Image.open(image_path)
    return image