from sequence import calculate_sequence, unpack_sequence
import numpy as np
import matplotlib.pyplot as plt


def generate_p_plots():
    p_list = np.arange(0.79, 1.08, 0.001)

    for p in p_list:
        calculate_sequence(0.25, 0.16, p)


def create_biffurcation_diagram():
    generate_p_plots()

    figure = plt.figure()
    axes = figure.add_subplot(111, projection='3d')
    axes.set_xlabel('x-axis')
    axes.set_ylabel('y-axis')
    axes.set_zlabel('p-axis')

    p_values = np.arange(0.79, 1.08, 0.001)
    for p in p_values:
        x_sequence = unpack_sequence(p, 'x')
        y_sequence = unpack_sequence(p, 'y')
        p_sequence = np.zeros(1000)

        for i in range(1000):
            p_sequence[i] = p

        axes.scatter(x_sequence, y_sequence, p_sequence, s=5)

    plt.show()


