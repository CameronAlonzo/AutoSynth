import numpy as np

'''
Base class
'''
class DataAugmentor:
    def augment(self, data, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")
'''
Noise Gen
'''
class NoiseAugmentor(DataAugmentor):
    def augment(self, data, noise_level=0.1):
        return data + noise_level * np.random.nomral(size=data.shape)