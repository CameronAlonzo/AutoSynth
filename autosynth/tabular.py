# autosynth/tabular.py
import numpy as np
import pandas as pd
from typing import *
#from autosynth/DataGenerator.py
from DataGenerator import *
'''
Class to handle tabular data generation
'''
class TabularDataGenerator(DataGenerator):
    def __init__(self, n_samples=100, n_features=5):
        self.n_samples = n_samples
        self.n_features = n_features

    def generate(self):
        X = np.random.rand(self.n_samples, self.n_features)
        y = np.random.choice([0, 1], size=self.n_samples)
        return pd.DataFrame(X), y
