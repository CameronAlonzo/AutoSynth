import numpy as np
import pandas as pd

def generate_synthetic_data(n_samples=100, n_features=5):
    X = np.random.rand(n_samples, n_features)
    Y = np.random.choice([0, 1], size=n_samples)
    return pd.DataFrame(X), Y