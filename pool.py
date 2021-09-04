from sequence import calculate_sequence, unpack_sequence, count_plot_values
import numpy as np
import matplotlib.pyplot as plt


def create_pool(p):
    for x in np.arange(0, 1, 0.1):
        for y in np.arange(0, 1, 0.1):
            calculate_sequence(x, y, 0.8)

            x_sequence = unpack_sequence(p, 'x')
            y_sequence = unpack_sequence(p, 'y')

            plt.scatter(x, y, s=5, c=count_plot_values(x_sequence, y_sequence))
            print(x, y)

    plt.show()