#!/usr/bin/env python3
"""Advanced task 100: scatter plot with a color gradient (colorbar)."""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Plot 2000 random points colored by elevation.

    Elevation z peaks at 40 m at the origin and falls off with the distance
    from it, so the points form a "mountain" seen from above. A colorbar maps
    each color to its elevation.
    """
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    plt.scatter(x, y, c=z)
    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.title('Mountain Elevation')

    cbar = plt.colorbar()
    cbar.set_label('elevation (m)')

    plt.show()
