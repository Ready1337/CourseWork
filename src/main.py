from biffurcation import create_biffurcation_diagram
from pool import create_pool
import numpy as np


def init():
    create_biffurcation_diagram()
    # Based on pictures of the bifurcation diagram
    for p in np.arange(0.9, 0.92, 0.01):
        create_pool(p)


if __name__ == '__main__':
    init()
