#autosynth/api.py
from tabular import TabularDataGenerator
from image import ImageDataGenerator
from text import TextDataGenerator

class AutoSynthAPI:
    def __init__(self, d_type):
        self.d_type = d_type
    
    def generate_data(self, **kwargs):
        if self.d_type == 'tabular':
            generator = TabularDataGenerator(**kwargs)
        elif self.d_type == 'image':
            generator = ImageDataGenerator(**kwargs)
        elif self.d_type == 'text':
            generator = TextDataGenerator(**kwargs)
        else:
            raise ValueError("Unsupported data type \n")
        
        return generator.generate()