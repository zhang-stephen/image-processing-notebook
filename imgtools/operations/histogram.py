#!/bin/python3

from typing import Union

import numpy as np
from matplotlib import pyplot as plt

from .algorithm import find_ceil_pow2


def histogram(im: Union[np.ndarray, list[list]], nrows: int = 1, ncols: int = 1, index: int = 1, *, title: str = ''):
    if index > ncols * nrows:
        raise ValueError(f'Invalid subplot index {index} for {nrows} rows and {ncols} columns')

    pixel_ceil = find_ceil_pow2(np.max(im))
    histo = np.zeros((pixel_ceil,))

    for pixel in np.nditer(im):
        histo[pixel] += 1

    plt.subplot(nrows, ncols, index)
    plt.bar(range(pixel_ceil), histo)

    if len(title) > 0:
        plt.title(title)

    if index == ncols * nrows:
        plt.show()


# EOF
