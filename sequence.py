from numba import njit
import numpy as np


@njit
def get_next_members(x0, y0, p):
    x = p * (3 * y0 + 1) * x0 * (1 - x0)
    y = p * (3 * x0 + 1) * y0 * (1 - y0)

    return x, y


def calculate_sequence(x0, y0, p):
    sequence_members_count = 11000

    sequence = np.zeros((1000, 2))

    x = x0
    y = y0

    for i in range(sequence_members_count):
        x, y = get_next_members(x, y, p)

        if x > 1000 or y > 1000:
            print('Sequence went to infinity!')
            np.save(f'sequence_p{p}', sequence)
            return

        if np.isnan(x) or np.isnan(y):
            print('NaN detected!')
            np.save(f'sequence_p{p}', sequence)
            return

        if i > 9999:
            sequence[i-10000][0] = x
            sequence[i-10000][1] = y

    np.save(f'sequence_p{p}', sequence)


def unpack_sequence(p, name):
    xy_sequence = np.load(f'sequence_p{p}.npy')

    sequence = np.zeros(1000)
    if name == 'x':
        for i in range(1000):
            sequence[i] = xy_sequence[i][0]
    else:
        for i in range(1000):
            sequence[i] = xy_sequence[i][1]

    return sequence


def count_plot_values(x_sequence, y_sequence):
    joined_sequence = list()
    for i in range(1000):
        joined_sequence.append((x_sequence[i], y_sequence[i]))

    count_list = list()

    for value in joined_sequence:
        if value not in count_list:
            count_list.append(value)

    return len(count_list)
