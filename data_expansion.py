from scipy import constants
import numpy as np

class Expansion:
  def __init__(self):
    pass

  def add_entropy(self, data, columns, num_values):
    sample = data.head(num_values)
    for col in columns:
      sample[col] = np.random.randint(low=constants.pi * 1000, high=constants.pi * 10000, size=num_values)
    return sample
