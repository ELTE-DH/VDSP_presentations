import numpy as np
import matplotlib.pyplot as plt

def linear_normalization(data):
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

# Example usage
data = np.array([0, 1, 2, 3, 4, 5])
normalized_data = linear_normalization(data)
print(normalized_data)

# Critical usage
data = np.array([1, 1, 1, 1, 1, 1])
normalized_data = linear_normalization(data)
print(normalized_data)

