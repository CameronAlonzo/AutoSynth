from PIL import Image, ImageDraw
from DataGenerator import *
import numpy as np

class ImageDataGenerator(DataGenerator):
    def __init__(self, image_size=(64, 64), n_images=100):
        self.image_size = image_size
        self.n_images = n_images
    
    def generate(self):
        images = []
        for _ in range(self.n_images):
            img = Image.new('RGB', self.image_size, color= (
                np.random.randint(255), 
                np.random.randint(255), 
                np.random.randint(255)
                ))
            images.append(img)
        return images