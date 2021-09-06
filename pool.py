from sequence import calculate_sequence, unpack_sequence, count_plot_values
import numpy as np
import matplotlib.pyplot as plt


def create_pool(p):

    for x in np.arange(0, 1, 0.01):
        for y in np.arange(0, 1, 0.01):
            calculate_sequence(x, y, p)

            x_sequence = unpack_sequence(p, 'x')
            y_sequence = unpack_sequence(p, 'y')

            color = count_plot_values(x_sequence, y_sequence)
            plt.scatter(x, y, s=5, c=color)
            print(x, y)

    plt.show()
