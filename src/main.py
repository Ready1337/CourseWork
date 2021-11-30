from biffurcation import create_biffurcation_diagram
from pool import create_pool
import numpy as np


def init():
    create_biffurcation_diagram()
    # The results of the bifurcation diagram
    # indicate the need to use the value 0.9 as the parameter p
    for p in np.arange(0.9, 0.92, 0.01):
        create_pool(p)


if __name__ == '__main__':
    init()
