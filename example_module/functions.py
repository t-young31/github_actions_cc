import numpy as np


def sqrt(x: float):
    """
    Take the square root of a positive number

    Arguments:
        x (int):

    Returns:
        (float): √x

    Raises:
        (ValueError): If the number is negative
    """
    if x < 0:
        raise ValueError('Cannot square-root a negative number with this '
                         'function!')

    return np.sqrt(x)
