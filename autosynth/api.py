#autosynth/api.py
from tabular import TabularDataGenerator
from image import ImageDataGenerator
from text import TextDataGenerator

class AutoSynthAPI:
    def __init__(self, d_type, **kwargs):
        self.d_type = d_type
        self.generator = self._initialize_generator(**kwargs)
    
    def _initialize_generator(self, **kwargs):
        if self.d_type == 'tabular':
            return TabularDataGenerator(**kwargs)
        elif self.d_type == 'image':
            return ImageDataGenerator(**kwargs)
        elif self.d_type == 'text':
            return TextDataGenerator(**kwargs)
        else:
            raise ValueError(f"Unsupported data type: {self.d_type} \n")
    
    def generate_data(self, augment=False, augmentor=None, **kwargs):
        if self.generator is None:
            raise RuntimeError("Generator is not initialized. Check data type.")
        if self.generator == 'tabular':
            data, labels = self.generator.generate()
        else:
            data = self.generator.generate()

        if augment and augmentor:
            data = augmentor.augment(data)

        return data

