import numpy as np

def make_pattern(shape=(16, 16), levels=1024):
    "Creates a pattern from gray values."
    return np.random.randint(0, levels - 1, shape) / levels
# For this function we use a random generation of values between 0 and 1, where 1 is white and 0 is black. 
