import numpy as np
import pandas as pd
from PIL import Image
'''
Base class
'''
class DataAugmentor:
    def augment(self, data, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")
'''
Noise Gen
'''
class Noise(DataAugmentor):
    def __init__(self, noise_level):
        self.noise_level = noise_level
    def augment(self, data):
        if isinstance(data, tuple):  # For tabular data
            tData, labels = data[0], data[1]
            noise = self.noise_level * np.random.normal(size=tData.shape)
            return pd.DataFrame(noise), labels
        
        elif isinstance(data, list):  # For text data
            noise = [self._add_noise_to_text(item) for item in data]
            return noise
        
        elif isinstance(data, list) and all(isinstance(img, Image.Image) for img in data):  # For image data
            return [self._add_noise_to_image(img, self.noise_level) for img in data]
        
        else:
            raise ValueError(f"Unsupported data type for augmentation. Expected Dataframe, or List, but recieved {data}")

    def _add_noise_to_text(self, text: list[list[str]]) -> list[str]:
        # Here you can implement text noise, e.g., random character insertion
        if not isinstance(text, list):
            print("augment argument was not of type: List")
            return text
        noisy_sentences = []
        for sentence in text:
            if np.random.randint(0, 100) < self.noise_level * 100:
                noisy_sentences.append(sentence + np.random.choice(list('abcdefghijklmnopqrstuvwxyz')))
            else:
                noisy_sentences.append(sentence)
        return noisy_sentences

    def _add_noise_to_image(self, img):
        # Convert the image to a NumPy array
        img_array = np.array(img)
        noise = self.noise_level * np.random.normal(size=img_array.shape)  # Create noise
        noisy_img_array = np.clip(img_array + noise, 0, 255)  # Add noise and clip to valid range
        return Image.fromarray(noisy_img_array.astype(np.uint8))  # Convert back to an image