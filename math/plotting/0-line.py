#!/usr/bin/env python3
"""Line graph of the cubes of the integers 0 to 10."""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plot y = x^3 for x in 0..10 as a solid red line."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, color='red', linestyle='-')
    plt.xlim(0, 10)
    plt.show()
