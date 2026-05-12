import numpy as np
#import random

def true_function(x):
    y = np.array(np.sin(np.pi * np.array(x) * 0.8) * 10)
    return y

def random_x( seed = 0, n = 20 ):
    np.random.seed(seed)
    x = np.random.uniform(-1, 1, n)
    return x

