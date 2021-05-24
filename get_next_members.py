from numba import njit
import numpy as np
import matplotlib


@njit
def get_next_members(x0, y0, p):
    x = p * (3 * y0 + 1) * x0 * (1 - x0)
    y = p * (3 * x0 + 1) * y0 * (1 - y0)
    print(x, y)

    return x, y


def calculate_sequence(x0, y0, p):
    sequence_members_count = 11001

    sequence = np.zeros((sequence_members_count, 2))

    x = x0
    y = y0

    for i in range(sequence_members_count):
        next_members = get_next_members(x, y, p)

        sequence[i][0] = next_members[0]
        sequence[i][1] = next_members[1]

        x = sequence[i][0]
        y = sequence[i][1]

        if x > 1000 or y > 1000:
            print('Sequence went to infinity!')
            return

        if np.isnan(x) or np.isnan(y):
            print('NaN detected!')
            return

        if i == 11000:
            xn = sequence[10001:11001, 0]
            yn = sequence[10001:11001, 1]

            np.save(f'sequence_p{p}', np.array([xn, yn]))
            loaded = np.load(f'sequence_p{p}.npy')
            print(loaded)


def generate_p_sequences():
    #chart = np.array[]
    #for p in np.arange(0, 2, 0.02):
    pass

    
